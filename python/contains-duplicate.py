class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = False
        for current_element in nums:
            current_count = 0
            for pivot in nums:
                if pivot == current_element:
                    current_count  = current_count + 1
            if current_count >= 2:
                result = True
        return result
