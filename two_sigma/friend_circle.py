# https://leetcode.com/problems/friend-circles/
'''
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
'''

#https://www.cnblogs.com/lightwindy/p/8667883.html
def solution(M):
    num_of_friend_circle = 0
    num_of_students = len(M)

    def DFS(M, row, col):
        # mark visited
        M[row][col] = 0
        M[col][row] = 0

        #  DF S neighbours
        for z in range(num_of_students):
            if M[row][z]:
                DFS(M, z, row)

    for row in range(num_of_students):
        for col in range(num_of_students):
            if M[row][col]:
                num_of_friend_circle += 1
                DFS(M, row, col)

    return num_of_friend_circle


def solution2(M):

    cnt, N = 0, len(M)
    visited = set()

    def dfs(n):
        # neighbours x
        for x in range(N):
            if M[n][x] and x not in visited:
                visited.add(x)
                dfs(x)

    for student_i in range(N):
        if student_i not in visited:
            cnt += 1
            dfs(student_i)

    return cnt

def solution3(M):
    cnt, N = 0, len(M)
    visited = set()

    def bfs(n):
        q = [n]
        while q:
            n = q.pop(0)
            for x in range(N):
                if M[n][x] and x not in visited:
                    visited.add(x)
                    q.append(x)

    for x in range(N):
        if x not in visited:
            cnt += 1
            bfs(x)

    return cnt


if __name__ == '__main__':
    adj_matrix = \
                [[1,1,0],
                [1,1,0],
                [0,0,1]]
    solution2(adj_matrix)
    print(solution(adj_matrix))