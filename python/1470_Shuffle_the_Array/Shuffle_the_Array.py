# 1470. Shuffle the Array
# Link : https://leetcode.com/problems/shuffle-the-array/

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuffled_list = []
        index_for_shuffled_list = 0
        for index in range(2*n):
            if index % 2:
                index_for_shuffled_list = index//2 + 2*n//2
                shuffled_list.append(nums[index_for_shuffled_list])
            else :
                index_for_shuffled_list = index//2
                shuffled_list.append(nums[index_for_shuffled_list])
        return shuffled_list

if __name__ == '__main__':
    # begin
    nums = [2,5,1,3,4,7]
    n = 3
    s = Solution()
    value = s.shuffle(nums, n)
    print(value)