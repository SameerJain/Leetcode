class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter 
        freq_map = Counter(nums)
        for value in freq_map.values():
            if value > 1:
                return True 
        return False