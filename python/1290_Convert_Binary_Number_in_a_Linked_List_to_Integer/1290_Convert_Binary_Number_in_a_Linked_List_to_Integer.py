# 1290. Convert Binary Number in a Linked List to Integer
# Difficulty : Easy(80.6%)
# Link : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Example 1:

# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10


# Result : Success
# Details :
# Runtime: 20 ms, faster than 69.01% of Python online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 12.7 MB, less than 64.47% of Python online submissions for Convert Binary Number in a Linked List to Integer.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        decimal_value = 0
        while True:
            decimal_value = 2*decimal_value + head.val
            head = head.next
            if head == None:
                break

