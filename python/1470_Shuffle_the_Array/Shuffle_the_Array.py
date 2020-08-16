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