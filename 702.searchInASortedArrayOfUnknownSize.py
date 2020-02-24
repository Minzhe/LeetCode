class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        lower, upper = 0, 1

        while reader.get(upper) <= target:
            lower = upper
            upper *= 2
        
        while lower <= upper:
            index = (lower + upper) // 2
            if reader.get(index) == target:
                return index
            elif reader.get(index) > target:
                upper = index - 1
            else:
                lower = index + 1
        
        return -1