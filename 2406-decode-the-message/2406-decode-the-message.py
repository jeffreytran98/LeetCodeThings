class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l',
        'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

        alphaMap = {}

        for letter in key:
            if letter.isspace():
                continue
            if letter not in alphaMap:
                alphaMap[letter] = alphabet.pop(0)
        alphaMap[" "] = " "
        
        result = ""
        for letter in message:
            result += alphaMap[letter]

        return result


