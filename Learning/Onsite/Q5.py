"""
Given a file containing unit conversion rates, write a function that converts one unit to another.
The file consists of JSON-like log entries where each entry specifies a conversion rate between two units.
Your function should support both direct conversions (e.g., meters to feet) and chained conversions (e.g., meters to inches through feet).
The function should load the conversion rates from the file, store them internally,
and handle conversion requests dynamically. The units can be measurements like meters, feet, inches, centimeters, etc.
Sample Log File Entries:

{"from": "meters", "to": "feet", "rate": 3.281}
{"from": "feet", "to": "inches", "rate": 12}
{"from": "centimeters", "to": "inches", "rate": 0.3937}
{"from": "meters", "to": "centimeters", "rate": 100}
Example Conversions:

convert("meters", "inches", 2) → 78.744
2 meters → 6.562 feet (using meters to feet conversion rate of 3.281)
6.562 feet → 78.744 inches (using feet to inches conversion rate of 12)
convert("centimeters", "inches", 100) → 39.37
100 centimeters → 39.37 inches (using centimeters to inches conversion rate of 0.3937)
convert("meters", "centimeters", 1) → 100

1 meter → 100 centimeters (using meters to centimeters conversion rate of 100)
"""
import json
from collections import defaultdict, deque
from functools import cache


@cache
def parse_json(path: str) -> dict[list]:
    # build conversion graph
    graph = defaultdict(list)
    # with open(path) as f:
    #     for line in f.readlines():
    #         start, end, rate = line['from'], line['end'], line['rate']
    #         graph[start].append((end, rate))
    #         # reverse rate
    #         graph[end].append((start, rate))
    with open(path) as f:
        for line in f:
            line = json.loads(line)
            start, end, rate = line['from'], line['to'], line['rate']
            graph[start].append((end, rate))
            # reverse rate
            graph[end].append((start, rate))

    return graph


def convert(start_unit, target_unit, value):
    unit_graph = parse_json('unit_conversion_rates.log')

    # graph tranversal using BFS
    queue = deque([(start_unit, value)])
    visited = set()

    while queue:
        current_unit, current_rate = queue.popleft()
        visited.add(next_unit)

        # check if we reach the dest
        if current_unit == target_unit:
            return current_rate

        for next_unit, rate in unit_graph[current_unit]:
            if next_unit not in visited:
                queue.append((next_unit, current_rate * rate))

    # unreachable
    return None

if __name__ == '__main__':
    unit_graph = parse_json('unit_conversion_rates.log')
    result = convert("meters", "centimeters", 1)
    print(result)
    result = convert("meters", "inches", 1)
    print(result)