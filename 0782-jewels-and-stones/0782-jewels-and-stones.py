class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hashMap = {}
        result = 0
        #Counts all your stones
        for stone in S:
            if stone not in hashMap:
                hashMap[stone] = 1
            else:
                hashMap[stone] += 1

        #Compare, see how many of your jewels are stones
        for jewel in J:
            #If one of my jewels is a stone
            if jewel in hashMap:
                result += hashMap[jewel]
        return result

        #This works but it slow, use a hashmap
        #return len([letter for letter in S if letter in J])


        