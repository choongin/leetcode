# 1431. Kids With the Greatest Number of Candies
# Link : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# Given the array candies and the integer extraCandies, 
# where candies[i] represents the number of candies that the ith kid has.

# For each kid check if there is a way to distribute extraCandies 
# among the kids such that he or she can have the greatest number of candies 
# among them. Notice that multiple kids can have the greatest number of candies.

# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: 
# Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
# Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
# Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
# Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
# Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 


# Result : Success
# Runtime: 28 ms, faster than 66.20% of Python online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 12.7 MB, less than 59.99% of Python online submissions for Kids With the Greatest Number of Candies.

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        max_candy = max(candies)
        results = [0]*len(candies)
        for i in range(len(candies)):
            candy_with_extra = candies[i] + extraCandies
            if candy_with_extra >= max_candy:
                results[i] = True
            else:
                results[i] = False  
        return results

if __name__ == '__main__':
    # begin
    candies = [4,2,1,1,2]
    extraCandies = 1
    s = Solution()
    value = s.kidsWithCandies(candies, extraCandies)
    print(value)


