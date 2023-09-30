class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter=defaultdict(int)
        ans=[]
        for i in nums:
            counter[i]+=1
        for i in nums:
            if counter[i-1] or counter [i+1] or counter[i]>1: continue
            ans.append(i)
        return ans