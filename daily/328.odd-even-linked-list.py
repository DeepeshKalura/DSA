#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
# TODO: Not be able to solve by yourself but still great learning

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return None

        odd:ListNode = head
        evenHead = even = head.next 
        
        while(even and even.next):

            odd.next = odd.next.next 
            odd = odd.next
            
            even.next = even.next.next
            even = even.next

        
        odd.next = evenHead


        return head
# @lc code=end

