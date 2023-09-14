class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0
        ones = 0
        inv_ends = deque()
        for i in range(N):
            one = nums[i] == 1
            if inv_ends and inv_ends[0] == i:
                inv_ends.popleft()
            if inv_ends:
                if len(inv_ends) % 2:
                    one = not one
            if not one and i <= N - k:
                count += 1
                one = True
                inv_ends.append(i + k)
            ones += one        
        return count if ones == N else -1