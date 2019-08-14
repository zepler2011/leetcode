"""
Definition for a undirected graph node

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def getAllNodes(self, node):
        allNodes = set([node])
        queue = []
        queue.append(node)

        while queue:
            curNode = queue.pop(0)
            for neighbor in curNode.neighbors:
                if neighbor in allNodes:
                    continue
                allNodes.add(neighbor)
                queue.append(neighbor)

        return allNodes

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return node

        root = node
        nodes = self.getAllNodes(node)
        newNodes = {}

        for n in nodes:
            newNode = UndirectedGraphNode(n.label)
            newNodes[newNode.label] = newNode

        for n in nodes:
            newNode = newNodes[n.label]

            for neighbor in n.neighbors:
                newNeighbor = newNodes[neighbor.label]
                newNode.neighbors.append(newNeighbor)

        return newNodes[root.label]
