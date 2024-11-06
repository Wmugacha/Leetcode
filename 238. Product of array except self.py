class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        result = [1] * n
        

    
test = Solution()
print(test.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(test.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))
print(test.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))
print(test.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]))