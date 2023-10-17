class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        childrenNodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in childrenNodes:
                root = i

        # keep track of visited nodes
        visited = set()
        # queue to keep track of in which order do we need to process nodes
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node in visited:
                return False

            # mark visited
            visited.add(node)

            # process node
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])

        # number of visited nodes == given number of nodes
        # if n != len(visited) => some nodes are unreachable/multiple different trees
        return len(visited) == n