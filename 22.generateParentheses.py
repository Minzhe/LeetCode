class Solution:
    def generateParenthesis(self, n):
        sol = [[] for i in range(n+1)]
        sol[0] = ['']
        for i in range(1, n+1):
            for j in range(i):
                sol[i] += ['(' + x + ')' + y for x in sol[j] for y in sol[i-j-1]]
        return sol[n]