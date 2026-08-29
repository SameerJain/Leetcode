from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Get the frequency of values using a map 
    # count the list of k most frequent using either a min heap or sorting and storing into a list 
    # Build the result list 
        freq_map: dict[int,int] = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1

        freq_tup = []
        for key,value in freq_map.items():
            freq_tup.append([key,value])
        freq_tup.sort(key=lambda item: item[1],reverse=False)

        result = []
        while len(result) < k:
            result.append(freq_tup.pop()[0])
        return result


def main() -> None:
    solution = Solution()

    assert solution.topKFrequent([1, 2, 2, 3, 3, 3], 2) == [3, 2]
    assert solution.topKFrequent([-1, -1, 2], 1) == [-1]

    print("All tests passed.")


if __name__ == "__main__":
    main()
