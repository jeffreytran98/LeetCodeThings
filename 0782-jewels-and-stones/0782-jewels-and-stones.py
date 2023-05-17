class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([letter for letter in S if letter in J])













        #This works
        #return len([i for i in S if i in J])

        