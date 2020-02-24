from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times, N, K):
        reach_time = [0] + [float('Inf')] * N
        Q = deque([(0, K)])
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        while Q:
            t, node = Q.popleft()
            if t < reach_time[node]:
                reach_time[node] = t
                for v, w in graph[node]:
                    Q.append((t + w, v))
        maxtime = max(reach_time)

        return maxtime if maxtime < float('Inf') else -1