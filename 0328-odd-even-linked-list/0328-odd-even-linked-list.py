# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        evenhead = head.next
        currodd = head
        curreven = head.next
        while( currodd.next and curreven.next):
            currodd.next = currodd.next.next
            curreven.next = curreven.next.next
            currodd = currodd.next
            curreven = curreven.next
        currodd.next = evenhead
        return head