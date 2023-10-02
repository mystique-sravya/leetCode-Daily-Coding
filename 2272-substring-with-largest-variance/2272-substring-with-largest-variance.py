class Solution:
    def largestVariance(self, s: str) -> int:
        counter = [0]*26

        for c in s:
            counter[ord(c)-97] += 1

        g=0

        for i in range(26):
            for j in range(26):
                if i==j or counter[i]==0 or counter[j]==0:
                    continue
                major = chr(97+i)
                minor = chr(97+j)
                major_count = 0
                minor_count = 0

                minor_remain = counter[j]

                for c in s:
                    if c==major:
                        major_count+=1
                    if c==minor:
                        minor_count+=1
                        minor_remain-=1

                    # print(major_count, minor_count)

                    if minor_count > 0:
                        g = max(g, major_count - minor_count)
                        
                    
                    if major_count < minor_count and minor_remain>0:
                        major_count = 0
                        minor_count = 0
        return g