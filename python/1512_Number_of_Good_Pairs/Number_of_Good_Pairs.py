# 1512. Number of Good Pairs
# Link : https://leetcode.com/problems/number-of-good-pairs/
#  Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Result : Success
# Details :
# Runtime: 28 ms, faster than 49.16% of Python online submissions for Number of Good Pairs.
# Memory Usage: 12.6 MB, less than 96.98% of Python online submissions for Number of Good Pairs.

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size_of_nums = len(nums)
        number_of_good_pair = 0
        for i in range(size_of_nums):
            for j in range(size_of_nums-i-1):
                if nums[i] == nums[j+i+1]:
                    number_of_good_pair += 1
                else:
                    continue
        return number_of_good_pair


if __name__ == '__main__':
    # begin
    example1_nums = [1,2,3,1,1,3]    
    example2_nums = [1,1,1,1]
    example3_nums = [1,2,3]
    s = Solution()
    value1 = s.numIdenticalPairs(example1_nums)
    value2 = s.numIdenticalPairs(example2_nums)
    value3 = s.numIdenticalPairs(example3_nums)

    print("Answer of example 1 : {}".format(value1))
    print("Answer of example 2 : {}".format(value2))
    print("Answer of example 3 : {}".format(value3))






