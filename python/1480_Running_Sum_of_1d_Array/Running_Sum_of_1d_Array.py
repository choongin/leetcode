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