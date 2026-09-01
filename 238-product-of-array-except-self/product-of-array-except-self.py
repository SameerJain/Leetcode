from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get list of suffix
        # get list of prefix
        # multiply them into a new array and return it
        n = len(nums)
        neigh =  [1 for _ in range(n)]
        abou = [1 for _ in range(n)]
        oscar = [1 for _ in range(n)]

        for i in range(1,n):
            abou[i] *= nums[i-1] * abou[i-1]
        for i in range(n-2,-1,-1):
            oscar[i] *= nums[i+1] * oscar[i+1]
        for i in range(n):
            neigh[i] *= oscar[i] * abou[i]
        return neigh

solution = Solution()

test = solution.productExceptSelf([1,2,3,4])
print(test)