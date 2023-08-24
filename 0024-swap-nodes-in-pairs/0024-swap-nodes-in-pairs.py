# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummyNode = ListNode()
        prevNode = dummyNode
        currNode = head

        while currNode and currNode.next:
            prevNode.next = currNode.next
            currNode.next = prevNode.next.next
            prevNode.next.next = currNode

            prevNode = currNode
            currNode = currNode.next

        return dummyNode.next