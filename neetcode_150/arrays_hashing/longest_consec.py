from typing import List 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        curr_count = 1
        max_count = 1
        for i in range(len(nums) - 1):
            next_num = nums[i + 1]
            print(f"next_num: {next_num}")
            if nums[i] == next_num - 1:
                curr_count += 1
                print(f"Number added to sequence. curr_count {curr_count}")
            elif nums[i] == next_num:
                print(f"number is same so lets continue")
                continue
            else:
                max_count = max(max_count, curr_count)
                curr_count = 1
        max_count = max(max_count, curr_count)
        return max_count

solution = Solution()

test = [0, 1, 1, 2, 3, 4, 5, 6]

print(solution.longestConsecutive(test))