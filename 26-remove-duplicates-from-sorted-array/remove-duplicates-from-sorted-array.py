class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = 0
        i = 0
        while i < (len(nums)):
            if i != len(nums) - 1 and nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                uniqueNums+=1
                i+=1
        return uniqueNums
                
        