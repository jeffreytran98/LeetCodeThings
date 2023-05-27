class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        '''
        Initial thoughts:
        create a hashmap where {height : name} (done)
        sort height (done)
        go through hashmap and create result 
        where result is names in descending order by people height
        '''

        someHash = {}
        for i in range(len(names)):
            someHash[heights[i]] = names[i]

        #Puts height in ascending order
        sortedHeights = sorted(list(someHash.keys()))
        #flips the list to descending order
        sortedHeights.reverse()

        result = []
        for height in sortedHeights:
            if height in someHash:
                result += [someHash[height]]

        return result