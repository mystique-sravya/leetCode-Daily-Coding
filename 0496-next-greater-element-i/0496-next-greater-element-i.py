class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        res = [-1]*n1
        for i in range(n1):
            if nums1[i] in nums2:
                j = nums2.index(nums1[i])
                print(j)
                for x in range(j+1,n2):
                    if nums2[j] < nums2[x]:
                        res[i] = nums2[x]
                        break
        return res