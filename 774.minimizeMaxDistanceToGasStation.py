import math

class Solution:
    def minmaxGasDist(self, stations, K):
        lower = (stations[-1] - stations[0]) / (K + len(stations) - 1)
        upper = max([(s2 - s1) for s1, s2 in zip(stations[:-1], stations[1:])])

        while lower + 1e-6 < upper:
            dist = (lower + upper) / 2
            num = self.minGasStations(stations, dist)
            print(dist, num)
            if num > K:
                lower = dist
            else:
                upper = dist
        
        return upper

    def minGasStations(self, stations, dist):
        num = 0
        for s1, s2 in zip(stations[:-1], stations[1:]):
            num += math.ceil((s2 - s1) / dist) - 1
        return num

stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 9
sol = Solution()
sol.minmaxGasDist(stations, K)