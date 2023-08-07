class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Summary Ranges
        Initialize an empty list to store the result ranges.
        Initialize variables start and end to track the current range.
        Iterate through each element in the sorted array:
        If the element is consecutive to the previous element (i.e., num == end + 1), update the end of the current range.
        Otherwise, if start and end are equal, add a single element range to the result list. Otherwise, add the current range to the result list.
        Reset start and end to the current element.
        After the loop, add the last remaining range (if any) to the result list.

        """
        if not nums:
            return []
        l = []
        s = nums[0]
        e = nums[0]
        for i in nums[1:]:
            if i == e+1:
                e = i
            else:
                if s == e:
                    l.append(str(s))
                else:
                    l.append(str(s)+'->'+str(e))
            
                s = i
                e = i
        if s == e:
            l.append(str(s))
        else:
            l.append(str(s)+'->'+str(e))
            
            
        return l
                
                
                
            