# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
        d,r = divmod(n,k)
        
        curr = head
        ans = []
        for i in range(k):
            root = curr
            for j in range(d+(i<r)-1):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            ans.append(root)
        return ans
            
        