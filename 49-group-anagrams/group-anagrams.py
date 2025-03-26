'''
create a dictionary to store every entry 
iterate through each string in the provided list 
sort the string to create a key for the anagram
join the result to form a string
append the original string to the list of anagrams with the same key 
convert the dictionary values to a list and return it
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())