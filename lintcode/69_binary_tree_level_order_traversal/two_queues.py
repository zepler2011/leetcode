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

        levelqueue1 = []
        levelqueue2 = []
        curr_level_queue = levelqueue1
        next_level_queue = levelqueue2

        curr_level_queue.append(root)

        while True:
            values = []
            while len(curr_level_queue) > 0:

                node = curr_level_queue.pop(0)
                if node is not None:
                    values.append(node.val)
                    if node.left is not None:
                        next_level_queue.append(node.left)
                    if node.right is not None:
                        next_level_queue.append(node.right)

            if len(values) > 0:
                retList.append(values)

            if len(curr_level_queue) == 0 and len(next_level_queue) == 0:
                #done
                break
            else:
                # swap the two bookkeeping queues and get to the next level:
                tmp_queue = curr_level_queue
                curr_level_queue = next_level_queue
                next_level_queue = tmp_queue

        return retList
