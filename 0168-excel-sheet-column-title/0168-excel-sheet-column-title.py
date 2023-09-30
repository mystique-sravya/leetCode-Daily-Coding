class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        result = ''
        while columnNumber > 0:
            # Calculate the remainder when dividing by 26
            remainder = (columnNumber - 1) % 26

            # Convert the remainder to a character (A=0, B=1, ..., Z=25)
            char = chr(ord('A') + remainder)

            # Add the character to the result string
            result = char + result

            # Update columnNumber to the quotient when dividing by 26
            columnNumber = (columnNumber - 1) // 26

        return result
