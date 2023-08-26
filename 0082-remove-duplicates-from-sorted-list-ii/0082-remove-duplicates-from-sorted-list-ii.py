# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        
        while fast:
            if fast.next != None and fast.next.val == fast.val:
                while fast.next != None and fast.next.val == fast.val:
                    fast = fast.next
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
                

        return dummy.next