# A Dynamic Programming based Python program for edit
# distance problem

# m, n -- no. of remaining characters
def lcs(str1, str2, m, n):
    # insert the len of str2 if str1 is empty
    if m == 0:
        return 0

    if n == 0:
        return 0

    # compare last character of str1 and str2
    if str1[m-1] == str2[n-1]:
        return 1 + lcs(str1, str2, m-1, n-1)

    else:

        # delte left
        return max(lcs(str1, str2, m-1, n), lcs(str1, str2, m, n-1))

def lcs_dp(str1, str2, m, n):

    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    
# Driver program
str1 = "sunday"
str2 = "saturday"

print(lcs(str2, str1, len(str2), len(str1)))
# This code is contributed by Bhavya Jain
