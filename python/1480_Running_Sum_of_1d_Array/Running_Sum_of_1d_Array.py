# 1480. Running Sum of 1D Array
# Link : https://leetcode.com/problems/running-sum-of-1d-array/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Sums = []
        sum = 0
        for num in nums:
            sum += num
            Sums.append(sum)
        return Sums



if __name__ == '__main__':
    # begin
    s = Solution()
    value = s.runningSum([1, 2, 3, 4])
    print(value)