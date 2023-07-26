class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum = 0
        c = 0
        for i in nums:
            if i % 6 == 0:
                sum += i
                c += 1
        if c ==0:
            return 0
        else:
            return sum // c