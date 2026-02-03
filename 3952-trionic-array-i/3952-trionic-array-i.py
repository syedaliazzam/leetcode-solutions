class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        index = 0
        while index < n - 1 and nums[index] < nums[index+1]:
            index+=1
        if index == 0:
            return False
        isup = index
        while index  < n - 1 and nums[index] > nums[index+1]:
            index+=1
        if isup == index:
            return False
        isdown = index
        while index + 1 < n and nums[index] < nums[index+1]:
            index+=1
        if isdown == index:
            return False
        return index == n-1