class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #always be better to choose the box with maximum number of units in it so that the overall number of units that can be put on truck is maximized
        boxTypes.sort(key= lambda a: -a[1] )
        max_units = 0
        for box in boxTypes:
            if truckSize < 0 : break
            max_units += min(truckSize, box[0]) * box[1]
            truckSize -= box[0]
        return max_units