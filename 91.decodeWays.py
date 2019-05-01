class Solution:
    def numDecodings(self, s):
        sol = [0 for i in range(len(s)+1)]
        sol[0] = 1
        sol[1] = int(s[0] != '0')
        
        for i in range(2, len(s)+1):
            if s[i-1] != '0': sol[i] += sol[i-1]
            if s[i-2] != '0' and int(s[i-2:i]) <= 26: sol[i] += sol[i-2]
        return sol[-1]