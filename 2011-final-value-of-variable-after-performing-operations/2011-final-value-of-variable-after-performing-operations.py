class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        add = ['++X','X++']
        sub = ['--X','X--']
        sum = 0
        for i in operations:
            if i in add:
                sum += 1
            if i in sub:
                sum -= 1
        return sum