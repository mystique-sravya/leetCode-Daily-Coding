# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry = 0
        while(l1 != None or l2 != None or carry == 1):
            s = 0
            if l1!= None:
                s += l1.val
                l1 = l1.next
            if l2 != None:
                s += l2.val
                l2 = l2.next
            
            s += carry
            carry =  s//10
            
            node = ListNode(s % 10)
            temp.next = node
            temp = temp.next
        return dummy.next
            
            
            