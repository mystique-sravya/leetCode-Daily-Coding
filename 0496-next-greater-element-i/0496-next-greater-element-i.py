class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        for i in range(0,len(nums1)):
            p = nums2.index(nums1[i])
            k = p+1
            while k < len(nums2):
                if nums2[k] > nums1[i]:
                    res[i] = nums2[k]
                    break
                k += 1
        return res