"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        start = 0
        end = 2
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            value = reader.get(mid)
            if value == 2147483647:
                return -1
            
            if value < target:
                start = mid
                end = mid + 2 * (end - start)
            elif value >= target:
                end = mid
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1
