class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        start = 0
        # end = ( houses[-1] - houses[0] ) // 2 + 1
        end = max(houses[-1], heaters[-1])
        # end = sys.maxsize
        
        while start +1 < end:
            mid = (start+end)//2
            
            if self.canWarm(houses, heaters, mid):
                end = mid
            else:
                start = mid
        
        # print start,end
        if self.canWarm(houses, heaters, start):
            return start
        else:
            return end 
        
        
    def canWarm(self, houses, heaters, R):
        # print R
        n,m = len(houses),len(heaters)
        i,j = 0,0
        
        while i < n and j < m:
            
            while i < n and abs(houses[i] - heaters[j]) <= R:
                i += 1
                    
            if i < n and j < m:
                j += 1 
                
        if i == n:
            return True
        else:
            return False