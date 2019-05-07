class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        Q = [[end]]
        notused = set(bank) - set([end])
        
        while Q:
            seq = Q.pop(0)
            gene = seq[-1]
            for i in range(len(gene)):
                for n in 'ATCG':
                    new = gene[:i] + n + gene[i+1:]
                    if new == start:
                        return len(seq)
                    elif new in notused:
                        Q.append(seq + [new])
                        notused.remove(new)
        return -1