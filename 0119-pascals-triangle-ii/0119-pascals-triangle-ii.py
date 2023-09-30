class Solution:
    def getRow(self, r: int) -> List[int]:
     
        ans = [1] * (r + 1)
        
        # Initialize variables for numerator and denominator
        up = r
        down = 1
        
        # Calculate the elements in the row
        for i in range(1, r):
            # Update the current element using the binomial coefficient formula
            ans[i] = ans[i - 1] * up // down  # Use integer division for Python 3
            
            # Update the numerator and denominator
            up -= 1
            down += 1
        
        return ans
