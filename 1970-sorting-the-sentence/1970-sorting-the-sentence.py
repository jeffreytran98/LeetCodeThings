class Solution:
    def sortSentence(self, s: str) -> str:
        #splits into a mutuable list
        listS = s.split()
        someHash = {}

        for word in listS:
            if word[-1:] not in someHash:
                someHash[word[-1:]] = word[:-1]
            else:
                pass
    
        resultList = []

        for i in range(1, len(someHash) + 1):
            if str(i) in someHash.keys():
                resultList += [someHash[str(i)]]
        temp = ' '
        result = temp.join(resultList)

        return result


