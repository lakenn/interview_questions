# https://www.google.com/search?sca_esv=2ac440225920b4d9&sca_upv=1&rlz=1C5CHFA_enHK937HK938&sxsrf=ADLYWIL0QILlsAo3TuaAHKXGVo6MEdHkEQ:1714851101110&q=leetcode+bus+routes&tbm=vid&source=lnms&prmd=ivnmbtz&sa=X&ved=2ahUKEwj7j-WV3vSFAxXuRUEAHcUFAqUQ0pQJegQIChAB&biw=1920&bih=895&dpr=2#fpstate=ive&vld=cid:c8c01f0e,vid:odmGyOJM5EY,st:0
import collections
from collections import defaultdict
from typing import List

# https://leetcode.com/problems/bus-routes/description/
""""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        visited = set()
        # eg. routes = [[bus1, bus2, ...], []]
        # bus stop to route dict
        for route_id, route in enumerate(routes):
            for bus_stop in route:
                graph[bus_stop].add(route_id)

        ans = 0
        queue = collections.deque([source])

        while queue:
            bus_stop = queue.popleft()
            ans += 1

            if bus_stop == target:
                return ans

            route = graph[bus_stop]

            for next_bus_stop in route:
                if next_bus_stop not in visited:
                    visited.add(next_bus_stop)
                    queue.append(next_bus_stop)

        return -1
