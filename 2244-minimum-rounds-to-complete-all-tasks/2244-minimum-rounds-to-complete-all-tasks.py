class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d=Counter(tasks)
        x=0
        for c in d.values():
            while c >0:
                if c>=3:c-=3
                elif c>=2:c-=2
                else:c-=1
                x+=1
        if any(count < 2 for count in d.values()):
            return -1             
        return x 