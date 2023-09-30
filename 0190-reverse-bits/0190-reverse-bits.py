class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):  # Iterate through 32 bits
            result <<= 1       # Left-shift the result by 1 bit
            result |= n & 1    # Set the least significant bit of result to the current bit of n
            n >>= 1            # Right-shift n by 1 bit
        return result
