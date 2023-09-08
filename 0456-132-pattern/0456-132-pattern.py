class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ak = min(nums)
        stack = []
        for num in nums[::-1]:
            if num < ak:
                return True
            while stack and num > stack[-1]:
                ak = stack.pop()
            stack.append(num)
        return False
            