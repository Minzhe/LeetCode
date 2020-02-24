import math

class Solution:
    def isStrobogrammatic(self, num):
        valid_pair = {('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')}
        pos = math.ceil(len(num) / 2)
        for i in range(pos):
            if (num[i], num[len(num) - 1 - i]) not in valid_pair:
                return False
        return True

num = "69"
sol = Solution()
sol.isStrobogrammatic(num)