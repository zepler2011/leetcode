class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        
        maxe = height[0]
        for i in range(n):
            if height[i] > maxe:
                maxe = height[i]
            leftMax[i] = maxe
            
        maxe = height[-1]
        for i in range(n-1, -1, -1):
            if height[i] > maxe:
                maxe = height[i]
            rightMax[i] = maxe 
            
        water = 0
        for i in range(n):
            if leftMax[i] < rightMax[i]:
                water += leftMax[i] - height[i]
            else:
                water += rightMax[i] - height[i]
                
        return water
        