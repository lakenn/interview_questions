from collections import defaultdict, deque

conversion_graph = defaultdict(list)

def parse_fact(facts):
    # build adj list
    for fact in facts:
        fact = fact.split()
        start, end, weight = fact[0], fact[-1], float(fact[2])
        conversion_graph[start].append((end, weight))
        conversion_graph[end].append((start, 1/weight))

    return conversion_graph

def answer_query(query, facts):
    fact_graph = parse_fact(facts)
    query = query.split()
    start_amt, start, end = float(query[0]), query[1], query[-1]

    visited = set()
    visited.add(start)
    queue = deque([(start, start_amt)])

    while queue:
        current_unit, current_weight = queue.popleft()
        if end == current_unit:
            return current_weight

        for neighbor, convert_weight in fact_graph[current_unit]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, convert_weight * current_weight))

    return -1

print(answer_query('2 m = ? in', ['m = 3.28 ft', 'ft = 12 in']))

