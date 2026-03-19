from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] == nums[end]:
                end -= 1
            else:
                start = mid + 1

        return nums[start]