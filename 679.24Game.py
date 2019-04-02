import itertools
class Solution:
    def judgePoint24(self, nums):
        perm = itertools.permutations(nums)
        symb = ['+', '-', '*', '/', '~-', '~/']
        comb_opers = [[x,y,z] for x in ['+', '-'] for y in ['*', '/'] for z in ['+', '-']]
        seq_opers = [[x,y,z] for x in symb for y in symb for z in symb]
        for num in perm:
            # combinatory calculation
            for oper in comb_opers:
                if self.calculate_comb(num, oper) == 24:
                    return num, oper
            # sequential calculation
            for oper in seq_opers:
                if self.calculate_seq(num, oper) == 24:
                    return num, oper
        return False
    
    def calculate_comb(self, nums, opers):
        part1 = (nums[0] + nums[1]) if opers[0] == '+' else (nums[0] - nums[1])
        part2 = (nums[2] + nums[3]) if opers[2] == '+' else (nums[2] - nums[3])
        if part2 == 0:
            return 0
        return (part1 * part2) if opers[1] == '*' else (part1 / part2)

    def calculate_seq(self, nums, opers):
        res = nums[0]
        for i in range(len(opers)):
            oper = opers[i]
            num = nums[i+1]
            if oper == '+':
                res += num
            elif oper == '-':
                res -= num
            elif oper == '*':
                res *= num
            elif oper == '/':
                res /= num
            elif oper == '~-':
                res = num - res
            else: # ~/
                if res == 0:
                    return 0
                else:
                    res = num / res
        return round(res, 6)

sol = Solution()
x = sol.judgePoint24([1, 1, 7, 7])
print(x)