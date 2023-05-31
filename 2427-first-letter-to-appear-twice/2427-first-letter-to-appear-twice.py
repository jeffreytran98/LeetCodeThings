class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashMap = {}

        for letter in s:
            if letter not in hashMap:
                hashMap[letter] = 1
            else:
                return letter

