class Solution:
    def decodeString(self, s):
        ans = [['', 1]]
        num = ''
        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                ans.append(['', num])
                num = ''
            elif char == ']':
                string, repeat = ans.pop()
                ans[-1][0] += string * int(repeat)
            else:
                ans[-1][0] += char
        return ans[0][0]