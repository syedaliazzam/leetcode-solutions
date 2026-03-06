# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Solution:
- Use BFS and level order approach to create a 2d list in level order.
- Return the reverse list.
- Time complexity : O(n)
- Space complexity : O(n)
'''

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        unvisited_list = deque()
        unvisited_list.append(root)
        result = []

        if root is None:
            return result

        while (len(unvisited_list) > 0):
            buffer = [] # List for same level nodes

            # Loop for level order
            for _ in range(len(unvisited_list)):
                current_node = unvisited_list.popleft() #FIFO

                if current_node is not None:
                    buffer.append(current_node.val)

                    # Generate successors.
                    left = current_node.left
                    right = current_node.right

                    if left: unvisited_list.append(left)
                    if right: unvisited_list.append(right)
        
            # Add nodes in buffer to the result.
            result.append(buffer)
        
        return result[::-1]
        