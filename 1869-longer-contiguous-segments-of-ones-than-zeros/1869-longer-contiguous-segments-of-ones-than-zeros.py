class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        mx_zero = 0
        mx_one = 0
        curr_zero = 0
        curr_one = 0

        for char in s:
            if char == '0':
                curr_zero += 1
                curr_one = 0  
            else:
                curr_one += 1
                curr_zero = 0  

            mx_zero = max(mx_zero, curr_zero)
            mx_one = max(mx_one, curr_one)

        return mx_one > mx_zero