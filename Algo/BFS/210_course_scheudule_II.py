from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the adjacence list
        graph = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            graph[u].append(v)

        # topological sorted order
        ans = []

        # visit node
        visited = [0 for _ in range(numCourses)]

        def dfs(node):
            if visited[node] == 1:  # the node has been visited
                return True
            elif visited[node] == -1:  # the node is being visited
                return False

            # the node has not been visited
            visited[node] = -1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            visited[node] = 1
            ans.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return list(reversed(ans))

print(Solution().findOrder(2, [[1, 0]]))