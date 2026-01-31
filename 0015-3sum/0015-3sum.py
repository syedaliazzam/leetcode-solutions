class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, numbers: List[int], i: int, res: List[List[int]]):
        start = i + 1
        end = len(numbers) - 1
        target = -numbers[i]
        while start < end:
            s = numbers[start] + numbers[end]
            if s == target:
                res.append([numbers[i], numbers[start], numbers[end]])
                # Skip duplicates for start
                while start < end and numbers[start] == numbers[start + 1]:
                    start += 1
                # Skip duplicates for end
                while start < end and numbers[end] == numbers[end - 1]:
                    end -= 1
                start += 1
                end -= 1
            elif s < target:
                start += 1
            else:
                end -= 1