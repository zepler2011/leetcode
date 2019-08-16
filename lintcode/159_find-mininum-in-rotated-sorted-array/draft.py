class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[end]:
                end  = mid
        
        return min(nums[start], nums[end])
        # note: doesn't work for [1, 2, 3]
