class Solution:
    def searchInsert(self, a: List[int], t: int) -> int:
        return bisect_left(a,t) 