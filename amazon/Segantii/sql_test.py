'''

Task
There is an events table used to track different key activities taken on a website. For this task you need to filter the name field to only show "trained" events. Events should be grouped by the day they happened and counted. The description field is used to distinguish which items the events happened on.

Along with the results, a time series chart will also be provided which will consume the data and be used to visualize the data. Create your query to be ready to be consumed by the chart, such as ensuring the dates are in order.

Table Schema
events
A table of events and the details of each event.

NAME	TYPE
id	INT
name	STRING
created_at	DateTime
description	String
Query Schema
Resulting query
A list of events ordered by their date with a count

NAME	TYPE
day	Date
description	String
count	INT
The expected results is provided so that you can see what the expected output is supposed to look like. Your "actual" output needs to match the expected output.

Testing Info
Dynamic Table Data
The data within each table is re-generated each time you submit. Do not expect to get the same data back twice.

In order to check accuracy of results, make sure to compare the actual results to the expected.

Test Errors
Tests are done using Ruby, which is why you may see some non-SQL looking errors if something isn't correct

'''

'''


select 
CAST(created_at AS DATE) as day, description, count(*)
from events
where
name = 'trained'
group by CAST(created_at AS DATE), description
order by CAST(created_at AS DATE) ASC

'''