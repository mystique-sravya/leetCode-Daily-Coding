class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        for combo in itertools.combinations(nums, k):
            if sum(combo) == n:
                result.append(list(combo))
        return result