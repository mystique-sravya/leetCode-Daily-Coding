class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_idx, pop_idx= 0, 0
        while push_idx < len(pushed):
            while stack and stack[-1]==popped[pop_idx]:
                stack.pop()
                pop_idx+=1
            stack.append(pushed[push_idx])
            push_idx+=1

        while stack:
            if stack[-1]!=popped[pop_idx]:
                return False
            else:
                stack.pop()
                pop_idx += 1
        return True