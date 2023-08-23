# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        node = head
        while node != None:
            node = node.next
            n += 1
        if (head == None or head.next == None or k == 1):
            return head
        dummy = ListNode(0)
        dummy.next =head
        pre = dummy
        curr = None
        nex = None
        
        while(n >= k):
            
            curr = pre.next
            nex = curr.next
            
            for  i in range(1,k):
                curr.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = curr.next
            pre = curr
            n = n-k
        return dummy.next
    
        
            