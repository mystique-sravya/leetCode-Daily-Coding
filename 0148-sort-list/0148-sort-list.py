# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findmiddle(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(list1, list2):
            newHead = tail = ListNode()
            while list1 and list2:
                if list1.val > list2.val:
                    tail.next = list2
                    list2 = list2.next
                else:
                    tail.next = list1
                    list1 = list1.next
                tail = tail.next

            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

            return newHead.next
        if not head or not head.next:
            return head
        
        left = head
        right = findmiddle(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return merge(left, right)
        