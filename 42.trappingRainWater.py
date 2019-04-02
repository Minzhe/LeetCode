def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    left_max, right_max, water = 0, 0, 0
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        if left_max <= right_max:
            water += left_max - height[left]
            left = left + 1
        else:
            water += right_max - height[right]
            right = right - 1
    return water
