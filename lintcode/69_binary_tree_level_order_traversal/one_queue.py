"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        retList = []

        queue = []
        curr_level_cnt = 0
        next_level_cnt = 0

        queue.append(root)
        curr_level_cnt += 1
        values = []

        while len(queue) > 0:

            node = queue.pop(0)
            curr_level_cnt -= 1
            if node is not None:
                values.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                    next_level_cnt += 1
                if node.right is not None:
                    queue.append(node.right)
                    next_level_cnt += 1

                if curr_level_cnt == 0:
                    curr_level_cnt = next_level_cnt
                    next_level_cnt = 0
                    retList.append(values)
                    values = []

        return retList
