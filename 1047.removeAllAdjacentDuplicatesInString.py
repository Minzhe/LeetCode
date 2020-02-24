class Solution:
    def removeDuplicates(self, S):
        stack = ['']
        for s in S:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)