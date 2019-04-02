def calculate(s):
    s += '+0'
    res, num, pre_oper = [], 0, '+'
    for x in s:
        if x.isdigit():
            num = 10 * num + int(x)
        elif x != ' ':
            if pre_oper == '+':
                res.append(num)
            elif pre_oper == '-':
                res.append(-num)
            elif pre_oper == '*':
                res.append(res.pop() * num)
            elif pre_oper == '/':
                res.append(int(res.pop() / num))
            num, pre_oper = 0, x
        print(res)
    return sum(res)

s = '14-3*2*2-1+2*2'
res = calculate(s)
print(res)

# def calculate(self, s):
#     digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     nums, opers = [], []
#     num = ''
#     for x in s:
#         if x is ' ':
#             continue
#         if x not in digits:
#             opers.append(x)
#             nums.append(int(num))
#             num = ''
#         else:
#             num += x
#     nums.append(int(num))
#     # calculate
#     res = [nums[0]]
#     for i in range(len(opers)):
#         oper = opers[i]
#         num = nums[i+1]
#         if oper == '+':
#             res.append(num)
#         elif oper == '-':
#             res.append(-num)
#         elif oper == '*':
#             res.append(res.pop()*num)
#         else:
#             res.append(int(res.pop()/num))
#     return sum(res)


        