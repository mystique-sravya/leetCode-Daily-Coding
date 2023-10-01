class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        x,y=0,0
        c=0
        res=0
        n=len(arr)
        for i in range(1,n-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                c=1
                x,y=i,i 
                while(y<n-1 and arr[y]>arr[y+1]):
                    c+=1 
                    y+=1
                while(x>0 and arr[x]>arr[x-1]):
                    c+=1 
                    x-=1
            res=max(c,res)
            c=0
        return res