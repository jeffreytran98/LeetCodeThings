class Solution:
    def findLucky(self, arr: List[int]) -> int:
        #Create a hashmap to count the number of occurences
        someHash = {}
        for i in arr:
            if i not in someHash:
                someHash[i] = 1
            else:
                someHash[i] += 1
        #the result is either -1 or the largest matching lucky number
        result = -1



        #go through the hashmap and if its a lucky number, set result to that
        for i in someHash:
            print(i, someHash[i])
            if i == someHash[i] and i > result:
                result = i
                
        return result