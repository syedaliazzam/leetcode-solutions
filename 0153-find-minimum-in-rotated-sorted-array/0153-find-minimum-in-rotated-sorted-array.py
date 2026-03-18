class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        Min=float('inf')
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<nums[r]:
                Min=min(Min,nums[mid])
                r=mid-1
            else:
                Min=min(Min,nums[mid])
                l=mid+1
        return Min