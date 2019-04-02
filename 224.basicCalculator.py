def calculate(s):
    num, sign, res, stack = 0, 1, 0, []
    for x in s:
        if x.isdigit():
            num = 10*num + int(x)
        elif x in ['+', '-']:
            res += num * sign
            sign = [-1, 1][x == '+']
            num = 0
        elif x == '(':
            stack.append(res)
            stack.append(sign)
            sign, res = 1, 0
        elif x == ')':
            res += num * sign
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + num * sign

s = " 1+4 - (5+6-(3-2)) +9 "
res = calculate(s)
print(res)