def verifyPreorder(preorder):
    left_leaf = []
    ancestor = float('-inf')
    for x in preorder:
        if x < ancestor:
            return False
        while left_leaf and x > left_leaf[-1]:
            ancestor = left_leaf.pop()
        left_leaf.append(x)
    return True
        


s = [5, 2, 6, 4, 3]
res = verifyPreorder(s)
print(res)