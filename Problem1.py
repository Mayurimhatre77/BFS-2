#In the rightSideView function, I solved the problem by using a breadth-first search (BFS) approach to traverse the binary tree level by level. Starting with the root node, I used a queue to keep track of nodes at each level. For each level, I added the value of the rightmost node to the result list. I processed each node by adding its left and right children to the queue for the next level. This ensured that I captured the rightmost node at each level, effectively building a view of the tree from the right side. The function handles each node once, resulting in a time complexity of O(n), and uses additional space for the queue and result list, giving a space complexity of O(n).

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        d = deque()
        d.append(root)
        ret = []
        while d:
            n = len(d)
            ret.append(d[-1].val)
            for i in range(n):
                cur = d.popleft()
                if cur.left:
                    d.append(cur.left)
                if cur.right:
                    d.append(cur.right)
                    
        return ret