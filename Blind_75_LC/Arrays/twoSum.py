'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Hint : use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in num_hash:
                return [num_hash[diff], index]
            num_hash[value] = index
        return None
a = Solution()
b = Solution()
print(a.twoSum([2,7,11,15], 9))
print(b.twoSum([3,2,4], 6))

