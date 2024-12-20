class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNums = [0] * len(nums) * 2
        for n in range(len(nums)):
            newNums[n] = nums[n]
            newNums[n+len(nums)] = nums[n] 
        return newNums