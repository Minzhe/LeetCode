class Solution:
    def numDecodings(self, s):
        one = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
        two = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '1*': 9,
               '20': 1, '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '2*': 6,
               '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2, '*5': 2, '*6': 2, '*7': 1, '*8': 1, '*9': 1, '**': 15}
        sol = [0 for i in range(len(s)+1)]
        sol[0] = 1
        sol[1] = one.get(s[0], 0)
        
        for i in range(2, len(s)+1):
            # decode last number
            add = one.get(s[i-1], 0) * sol[i-1]
            # decode last two number
            add += two.get(s[i-2:i], 0) * sol[i-2]
            sol[i] += int(add % (1e9+7))
        return sol[-1]

