class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(arr, day, m , k):
            n = len(arr)  # size of the array
            cnt = 0
            noOfB = 0
            # count the number of bouquets
            for i in range(n):
                if arr[i] <= day:
                    cnt += 1
                else:
                    noOfB += cnt // k
                    cnt = 0
            noOfB += cnt // k
            return noOfB >= m
        
        if m * k  > len(bloomDay):
            return -1
        
        l = min(bloomDay)
        h = max(bloomDay)
    
        while l <= h:
            mid = (l+h)// 2
            
            if feasible(bloomDay,mid, m , k) == True:
                h = mid - 1
            else:
                l = mid + 1
        return l
                