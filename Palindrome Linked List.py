# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        copy = slow
        ptr1, ptr2 = head, self.reverseLL(slow)
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1, ptr2 = ptr1.next, ptr2.next
        return True
    
    def reverseLL(self, slow):
        prev = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        slow = prev
        return slow
