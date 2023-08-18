class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True]*n
        primes[0] = primes[1] = False
        for i in range(2,n):
            if primes[i]:
                for m in range(2*i, n , i):
                    primes[m] = False
        return sum(primes)