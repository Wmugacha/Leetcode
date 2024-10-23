class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store numbers and their indices
        list_map = {}

        # Loop through the array
        for i, num in enumerate(nums):

            #Calculate the difference between the target and the current number
            diff = target - num

            # Check if the difference already exists in the dictionary
            if diff in list_map:
                
                # If it exists, return the indice of the current number and the indice of the diff
                return [i, list_map[diff]]

            # If it doesn't exist, add the current number and it's index to the disctionary
            list_map[num] = i

        # If no two numbers add up to the target, return None
        return None
    
# Test cases
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(s.twoSum([3, 2, 4], 6)) # [1, 2]
print(s.twoSum([3, 3], 6)) # [0, 1]
print(s.twoSum([3, 2, 3], 6)) # [0, 2]
print(s.twoSum([3, 2, 4], 7)) # [0, 2]