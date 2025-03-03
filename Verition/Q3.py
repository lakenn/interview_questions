-- Implement your solution here
WITH dummy_transactions AS (
    SELECT generate_series(
        '2020-01-01'::date,  -- Start date
        '2020-12-01'::date,  -- End date
        '1 month'::interval
    ) AS date,
    0 AS amount
),
all_transactions AS (
    SELECT date, amount
    FROM transactions
    UNION ALL
    SELECT date, amount
    FROM dummy_transactions
),
monthly_summary as (
    SELECT
        date_trunc('month', date) as month,
        SUM(amount) as monthly_balance,
        COUNT(CASE WHEN amount < 0 THEN 1 END) as spending_count,
        SUM(CASE WHEN amount < 0 THEN amount ELSE 0 END) as total_spending
    FROM all_transactions
    GROUP BY date_trunc('month', date)
),
monthly_balance_with_fees as (
    SELECT
        month,
        monthly_balance,
        CASE
            WHEN spending_count >= 3 AND total_spending <= -100 THEN 0
            ELSE 5
        END AS fees
    FROM monthly_summary
)
-- SELECT * FROM monthly_summary;

SELECT SUM(monthly_balance) - SUM(fees) AS balance
FROM monthly_balance_with_fees;



-- Calculate the final balance after accounting for fees
SELECT
    SUM(monthly_balance) - SUM(fees) AS balance
FROM (
    -- Determine monthly balances and applicable fees
    SELECT
        month,
        monthly_balance,
        CASE
            WHEN spending_count >= 3 AND total_spending <= -100 THEN 0
            ELSE 5
        END AS fees
    FROM (
        -- Summarize transactions by month
        SELECT
            date_trunc('month', date) AS month,
            SUM(amount) AS monthly_balance,
            COUNT(CASE WHEN amount < 0 THEN 1 END) AS spending_count,
            SUM(CASE WHEN amount < 0 THEN amount ELSE 0 END) AS total_spending
        FROM (
            -- Combine actual transactions with dummy transactions
            SELECT date, amount FROM transactions
            UNION ALL
            SELECT generate_series(
                '2020-01-01'::date,  -- Start date
                '2020-12-01'::date,  -- End date
                '1 month'::interval
            ) AS date, 0 AS amount
        ) AS all_transactions
        GROUP BY date_trunc('month', date)
    ) AS monthly_summary
) AS monthly_balance_with_fees;
