import collections
class Solution:
    def numBusesToDestination(self, routes, S, T):
        # what bus arrive at each stop
        stopBoard = collections.defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopBoard[stop].add(bus)
        # start route
        Q = [(S, 0)]
        visited = set([S])
        for cur, num in Q:
            print(Q)
            if cur == stop: return num
            for bus in stopBoard[cur]:
                for stop in routes[bus]:
                    if stop not in visited:
                        visited.add(stop)
                        Q.append((stop, num+1))
                routes[bus] = []
        return -1

routes = [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]]
S, T = 37, 28
sol = Solution()
res = sol.numBusesToDestination(routes, S, T)
print(res)