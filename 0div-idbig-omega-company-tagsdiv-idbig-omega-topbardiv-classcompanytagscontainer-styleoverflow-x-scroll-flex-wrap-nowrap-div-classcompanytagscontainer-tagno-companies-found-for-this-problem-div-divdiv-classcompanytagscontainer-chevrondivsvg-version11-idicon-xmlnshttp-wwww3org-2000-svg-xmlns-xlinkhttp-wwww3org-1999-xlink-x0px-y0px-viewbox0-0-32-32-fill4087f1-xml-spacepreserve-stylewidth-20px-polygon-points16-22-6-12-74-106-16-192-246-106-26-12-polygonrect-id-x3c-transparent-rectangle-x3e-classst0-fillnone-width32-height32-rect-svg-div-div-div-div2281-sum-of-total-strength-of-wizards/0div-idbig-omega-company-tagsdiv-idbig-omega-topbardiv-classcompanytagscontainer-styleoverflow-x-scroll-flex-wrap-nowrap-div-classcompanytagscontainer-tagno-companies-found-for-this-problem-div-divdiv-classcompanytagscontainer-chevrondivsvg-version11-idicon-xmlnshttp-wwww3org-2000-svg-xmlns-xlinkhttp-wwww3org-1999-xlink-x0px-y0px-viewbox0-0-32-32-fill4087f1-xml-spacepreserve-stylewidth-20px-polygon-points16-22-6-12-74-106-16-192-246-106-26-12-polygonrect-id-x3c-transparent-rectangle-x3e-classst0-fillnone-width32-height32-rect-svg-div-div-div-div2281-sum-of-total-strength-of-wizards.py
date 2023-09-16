class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        next_min_right = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                next_min_right[stack.pop()] = i
            stack.append(i) 
        next_min_left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                next_min_left[stack.pop()] = i
            stack.append(i) 
        prefixsum = [0] * n
        prefixsumsum = [0] * (n + 1)  

        for i in range(n):
            prefixsum[i] = prefixsum[i-1] + strength[i] if i > 0 else strength[i]
        for i in range(0, n):
            prefixsumsum[i+1] = prefixsumsum[i + 1 -1] + prefixsum[i]
        strength_sum = 0
        for i in range(n):
            left, right = next_min_left[i], next_min_right[i]
            len_left = i - left
            r_sum = prefixsumsum[right] - prefixsumsum[i] 
            len_right = right - i
            l_sum = prefixsumsum[i] - prefixsumsum[max(left, 0)] 
            strength_sum += strength[i] * (len_left * r_sum - len_right * l_sum)
        
        return strength_sum % (10**9 + 7)