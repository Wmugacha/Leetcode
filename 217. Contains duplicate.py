class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


test = Solution()
print(test.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(test.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))
print(test.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))
print(test.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]))