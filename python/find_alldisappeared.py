class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        all_ranges = range(size)
        all_ranges.remove(0)
        all_ranges.append(size)
        result = []
        for i in all_ranges:
            if i not in nums:
                result.append(i)
        return result
