class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        build a frequency map of elements 
        create ans list 
        iterate thru map k times, removing the max each time 
        '''
        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i],0) + 1
        
        ans = []
        while k > 0:
            max_val = 0
            max_key = 0
            for key,value in freq_map.items():
                if value > max_val:
                    max_key = key
                    max_val = value
            ans.append(max_key)
            del freq_map[max_key]
            k -=1

        return ans
