"""
In the first part, you were likely asked to determine if a string of parentheses is balanced or valid.
For example, the string "()" is balanced, while the string "(()" is not.

"""

str1 = "(()"

# 1st attempt
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                bracket = stack.pop()
                if (char == ')' and bracket != '(') or \
                        (char == ']' and bracket != '[') or \
                        (char == '}' and bracket != '{'):
                    return False

        return True if len(stack) == 0 else False

# 2nd attempt
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif len(stack) == 0 or bracket_map.get(char) != stack.pop():
                return False

        return False if len(stack) else True

# follow up
# Then he gave me a follow up to solve it without using a stack


# if there is only one bracket type

class Solution:
    def isValid(self, s:str) -> bool:
        count = 0

        for char in s:
            if char == "(":
                count += 1
            else:
                count -= 1

                if count < 0:  # we get a closing bracket first or more closing bracket found
                    return False

        return count == 0