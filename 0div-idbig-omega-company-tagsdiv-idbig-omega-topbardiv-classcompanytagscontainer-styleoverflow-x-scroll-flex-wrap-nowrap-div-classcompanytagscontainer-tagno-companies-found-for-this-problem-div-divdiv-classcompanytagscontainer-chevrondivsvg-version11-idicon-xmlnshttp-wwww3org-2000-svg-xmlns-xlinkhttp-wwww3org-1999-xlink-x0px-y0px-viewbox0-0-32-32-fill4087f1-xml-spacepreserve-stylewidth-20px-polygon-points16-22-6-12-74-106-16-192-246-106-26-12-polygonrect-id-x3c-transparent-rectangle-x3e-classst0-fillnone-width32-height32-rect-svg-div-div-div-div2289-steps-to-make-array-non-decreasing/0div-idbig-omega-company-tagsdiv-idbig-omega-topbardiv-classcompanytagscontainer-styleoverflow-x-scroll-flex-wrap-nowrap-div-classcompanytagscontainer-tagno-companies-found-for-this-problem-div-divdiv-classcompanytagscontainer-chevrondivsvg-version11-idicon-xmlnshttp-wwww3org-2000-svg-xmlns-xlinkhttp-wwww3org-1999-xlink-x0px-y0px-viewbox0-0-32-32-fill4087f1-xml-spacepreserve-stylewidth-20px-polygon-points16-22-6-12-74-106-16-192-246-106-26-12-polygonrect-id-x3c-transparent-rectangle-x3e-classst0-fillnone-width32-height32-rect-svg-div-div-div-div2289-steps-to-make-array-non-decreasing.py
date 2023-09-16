class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        st = []
        for i in range(n-1,-1,-1):
            c = 0
            while(st and nums[i] >st[-1][0]):
                c = max(c +1 , st[-1][-1])
                st.pop()
            ans = max(ans,c)
            st.append((nums[i],c))
        return ans