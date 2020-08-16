# 1. Two Sum
# Link : https://leetcode.com/problems/two-sum/

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        hash_nums = {}
        results = []
        for index, num in enumerate(nums):
            another = target - num
            try:
                hash_nums[another]                      # check counterpart is already in the list 
                return [hash_nums[another],index]
            except KeyError:                            # counterpart is not yet listed
                hash_nums[num] = index
        return results



if __name__ == '__main__':
    # begin
    s = Solution()
    value = s.twoSum([1, 5], 6)
    print(value)