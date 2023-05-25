class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        #Count # of character occurences in s
        hashMap = {}
        for letter in s:
            if letter not in hashMap:
                hashMap[letter] = 1
            else:
                hashMap[letter] += 1

        #Make hashMap.keys() into a set. If the len(set) != hashMap.keys(), it must false
        valueSet = set(hashMap.values())
        if len(valueSet) == 1:
            return True
        else:
            return False

