class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l = ["0"]*len(score)
        asc_score = sorted(score , reverse = True)
        for i in range(len(score)):
            if i == 0:
                f = score.index(asc_score[0])
                l[f] = "Gold Medal"
            elif i == 1:
                s = score.index(asc_score[1])
                l[s] = "Silver Medal"
            elif i == 2:
                b = score.index(asc_score[2])
                l[b] = "Bronze Medal"
            else:
                l[score.index(asc_score[i])] = str(i+1) 
        return l
            
        