from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq
        course_map = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            course_map[course].append(pre)

        visited = set()

        def dfs(course_id):
            if course_id in visited:
                # detect a cycle
                return False


            visited.add(course_id)
            # dfs backtracking
            if not any(dfs(pre_course_id) for pre_course_id in course_map[course_id]):
                return False

            visited.remove(course_id)
            # course_map[course_id] = []
            return True

        for course_id in range(numCourses):
            if not dfs(course_id): return False
        return True

Solution().canFinish()
