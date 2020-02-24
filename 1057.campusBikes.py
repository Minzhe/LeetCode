import heapq

class Solution:
    def assignBikes(self, workers, bikes):
        dist = [None for _ in workers]
        for w, w_cords in enumerate(workers):
            q = []
            for b, b_cords in enumerate(bikes):
                d = abs(w_cords[0] - b_cords[0]) + abs(w_cords[1] - b_cords[1])
                q.append((d, w, b))
            heapq.heapify(q)
            dist[w] = q
        
        min_dist = [heapq.heappop(q) for q in dist]
        heapq.heapify(min_dist)
        worker_to_bike = dict()
        used_bikes = set()

        while len(worker_to_bike) < len(workers):
            d, w, b = heapq.heappop(min_dist)
            if b not in used_bikes:
                worker_to_bike[w] = b
                used_bikes.add(b)
            else:
                heapq.heappush(min_dist, heapq.heappop(dist[w]))
        
        return [worker_to_bike[w] for w in sorted(worker_to_bike)]

workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
sol = Solution()
ans = sol.assignBikes(workers, bikes)
print(ans)