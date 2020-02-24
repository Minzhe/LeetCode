class Solution:
    def minAreaRect(self, points):
        min_area = float('Inf')
        seen = set()
        for (x1, y1) in points:
            for (x2, y2) in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    if area < min_area:
                        min_area = area
            seen.add((x1, y1))
        return 0 if min_area == float('Inf') else min_area