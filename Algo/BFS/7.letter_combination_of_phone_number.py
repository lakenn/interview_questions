L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}


def letterCombination(digits):
    ans = []

    def dfs(index, st):
        # accumulate enough chars
        if index == len(digits):
            ans.append(st)
            return

        # traverse each possible choices
        letters = L[digits[index]]
        for char in letters:
            dfs(index+1, st+char)

    dfs(0, '')
    return ans

letterCombination('')




