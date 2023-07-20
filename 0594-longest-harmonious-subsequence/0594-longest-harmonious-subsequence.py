class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        print(counts)
        longest = 0
        for count in counts:
            if count + 1 in counts:
                longest = max(longest, counts[count] + counts[count + 1])
        return longest

                