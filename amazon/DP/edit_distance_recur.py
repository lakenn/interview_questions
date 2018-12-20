# A Dynamic Programming based Python program for edit
# distance problem

# m, n -- no. of remaining characters
def editDistDP(str1, str2, m, n):
    # insert the len of str2 if str1 is empty
    if m == 0:
        return n

    # delete the len of str1 if str2 is empty
    if n == 0:
        return m

    # compare last character of str1 and str2
    if str1[m-1] == str2[n-1]:
        return editDistDP(str1, str2, m-1, n-1)

    else:

        # replace
        replace_num = 1 + editDistDP(str1, str2, m-1, n-1)

        # insert
        insert_num = 1 + editDistDP(str1, str2, m, n-1)

        # delete
        del_num = 1 + editDistDP(str1, str2, m-1, n)

        return min(replace_num, insert_num, del_num)

def editDistDP_bottom_up(str1, str2, m, n):
    pass


# Driver program
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str2, str1, len(str2), len(str1)))
# This code is contributed by Bhavya Jain
