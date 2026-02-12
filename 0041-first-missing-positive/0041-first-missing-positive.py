class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        filternums=set()
        for i in nums:
            if i>0:
                filternums.add(i)
        filternums=list(filternums)
        filternums.sort()
        for i in range(0,len(filternums)):
            if filternums[i]!=i+1:
                return i+1
        return len(filternums)+1
        
        