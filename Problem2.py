#In this code, I implemented the isCousins function to determine if two nodes, x and y, are cousins in a binary tree. Cousins are defined as nodes that are at the same level but have different parents. I used a breadth-first search (BFS) approach with a queue to traverse the tree level by level, keeping track of each node's level and parent. I initialized a queue with the root node, its level (0), and its parent (None). As I traversed each level, I checked if the current node's value matches x or y and recorded their level and parent information. I continued this process until I found both nodes. After the traversal, I checked if x and y are at the same level and have different parents, returning True if they are cousins and False otherwise. The time complexity of this solution is O(n) because each node is visited once, and the space complexity is also O(n) due to the queue storing nodes for each level of the tree.

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return

        queue = deque([(root, 0, None)])
        levelForX = levelForY = (-1, None)

        while queue:
            for _ in range(len(queue)):
                node, level, parent = queue.popleft()
                if node.val == x:
                    levelForX = (level + 1, parent)
                if node.val == y:
                    levelForY = (level + 1, parent)
                if node.left:
                    queue.append((node.left, level + 1, node))
                if node.right:
                    queue.append((node.right, level + 1, node))

        if levelForX[0] == levelForY[0] and levelForX[1] != levelForY[1]:
            return True

        return False