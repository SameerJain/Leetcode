from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return ""

        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        '''
        store int value of word 
        move j up that many places

        append i:j to result list 
        '''
        result = []

        if not s:
            return result

        i = 0
        while i < len(s)-1:
            print(result)
            j = i 
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            j = i + length 
            result.append(s[i+1:j+1])
            if j == len(s) - 1:
                break
            j+= 1
            i = j

        

        return result


solution = Solution()

test = solution.encode(["Hello","World"])
print(test)
print(solution.decode(test))
