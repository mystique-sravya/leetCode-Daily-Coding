class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s=set([int(i,2) for i in nums])
        maxlen=len(nums[0])
        for i in range(pow(2,maxlen)):
            if(i not in s):
                r=bin(i)[2:]
                return "0"*(maxlen-len(r))+r
        return "-1"