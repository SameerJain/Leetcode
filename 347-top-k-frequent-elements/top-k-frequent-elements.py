class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

        freq_map = sorted(freq_map.items(), key=lambda x: x[1],reverse=False)

        ans = []
        while len(ans) < k:
            ans.append(freq_map.pop()[0])

        return ans