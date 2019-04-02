def calculate(s):
    s += '+0'
    stack = []
    res, num, sub = 0, 0, 0
    opers, last_oper = [], '+'
    for x in s:
        if x == ' ': continue
        elif x.isdigit():
            num = 10 * num + int(x)
        elif x in ['+', '-', '*', '/']:
            if last_oper == '+':
                stack[-1].append(num)
            if last_oper == '-':
                stack[-1].append(-num)
            if last_oper == '*':
                stack[-1].append(stack[-1].pop()*num)
            if last_oper == '/':
                stack[-1].append(int(stack[-1].pop()/num))
            num, last_oper = 0, x
            sub = sum(stack[-1])
        elif x == '(':
            stack.append(sub)
            opers.append(last_oper)
        elif x == ')':
            if 
    return sum(sub)


s = "(2+6* 3+5- (3*14/7+2)*5)+3"
s = " 1+4 - (5+6-(3-2)) +9 "
s = "14-3*2-1"
res = calculate(s)
print(res)