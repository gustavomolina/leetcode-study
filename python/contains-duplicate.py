class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_numbers = set()

        for current_number in nums:
            if current_number in unique_numbers:
                return True
            else:
                unique_numbers.add(current_number)
