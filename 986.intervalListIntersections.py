class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def intervalIntersection(self, A, B):
        inter = []
        while len(A) > 0 and len(B) > 0:
            a_start, a_end = A[0].start, A[0].end
            b_start, b_end = B[0].start, B[0].end
            if a_start <= b_start:
                if a_end < b_start:
                    # a: [1,4], b: [5,6]
                    A.pop(0)
                else:
                    if a_end >= b_end:
                        # a: [1,4], b: [2,3]
                        inter.append([b_start, b_end])
                        B.pop(0)
                    else:
                        # a: [1,4], b: [2,5]
                        inter.append([b_start, a_end])
                        A.pop(0)
            else:
                if b_end < a_start:
                    # a: [1,4], b: [-1,0]
                    B.pop(0)
                else:
                    if b_end >= a_end:
                        # a: [1,4], b: [-1,5]
                        inter.append([a_start, a_end])
                        A.pop(0)
                    else:
                        # a: [1,4], b: [-1,3]
                        inter.append([a_start, b_end])
                        B.pop(0)
        print(inter)
        return [Interval(item[0], item[1]) for item in inter]
