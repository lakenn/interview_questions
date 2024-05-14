import collections
from typing import List

# https://techsauce.medium.com/unlocking-the-mystery-of-keys-and-rooms-%EF%B8%8F-5236c49a6121

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def bfs():
            queue = collections.deque([0])
            visited.add(0)

            while queue:
                node = queue.popleft()
                visited.add(node)
                for room_key in rooms[node]:
                    if room_key not in visited:
                        print(room_key)
                        queue.append(room_key)

        def dfs(room):
            print(room)
            visited.add(room)

            for room_key in rooms[room]:
                if room_key not in visited:
                    dfs(room_key)

        # dfs(0)
        bfs()
        return len(visited) == len(rooms)


print(Solution().canVisitAllRooms([[1],[2],[3],[]]))
