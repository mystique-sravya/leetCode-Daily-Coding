class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        ans = []
        for i in d:
            if d[i]> (len(nums)//3):
                ans.append(i)
        return ans
    
                
                
                
                
        