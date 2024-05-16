"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_final = len(nums) + 1
        result = 0
        for current_number in range(num_final):
            if current_number not in nums:
                result = current_number
        
        return result
