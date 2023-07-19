class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        area = 0
        
        while l < r:
            a = min(height[r], height[l]) * (r-l)
            area = max(a, area)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
                
        return area