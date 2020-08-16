
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