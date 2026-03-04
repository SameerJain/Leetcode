class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Use binary search 
        '''
        l = 0
        r = len(numbers) - 1

        while l <= r:
            mid = (l+r)//2 
            sum_val = numbers[l] + numbers[r]
            if  sum_val == target:
                return [l+1,r+1]
            elif sum_val < target:
                l += 1
            else:
                r-= 1
        return []