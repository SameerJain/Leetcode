class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for k in range(n+1,len(nums)):
                if nums[n] + nums[k] == target:
                    return[n,k]
        return []