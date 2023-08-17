class Solution:
    def trap(self, height: List[int]) -> int:
        l = [height[0]]
        res = 0
        for i in range(1,len(height)):
            l.append(max(l[-1],height[i]))
        r = [height[-1]]
        for i in range(len(height)-2,-1,-1):
            r.append(max(r[-1],height[i]))
        r.reverse()
        for i in range(1,len(height)-1):
            res = res + min(l[i],r[i])-height[i]
        print(l)
        print(r)
        return res