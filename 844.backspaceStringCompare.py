class Solution:
    def backspaceCompare(self, S, T):
        def get_string(S):
            string = []
            for s in S:
                if s == '#':
                    string = string[:-1]
                else:
                    string.append(s)
            return ''.join(string)
        
        return get_string(S) == get_string(T)