import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        queue = []        
        for p in points:
            d = self.dist(p[0], p[1])
            heapq.heappush(queue, (d, p))
            
        ret = []
        for _ in range(K):
            d, p = heapq.heappop(queue)
            ret.append(p)
            
        return ret
    
    def dist(self, v1, v2):
        return v1*v1 + v2*v2
