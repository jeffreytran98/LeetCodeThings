class Solution:
    def sortSentence(self, s: str) -> str:
        #splits into a mutuable list
        listS = s.split()

        #Create a hash table/dictionary to help sort/organize
        someHash = {}

        for word in listS:
            '''
            If the last "letter/digit" isn't in your hash table, add the word to the hash without the last "letter/digit"
            '''
            if word[-1:] not in someHash:
                someHash[word[-1:]] = word[:-1]
            else:
                pass
    
        resultList = []
        #From least to greatest (1-9), add the value to a List of strings (ordered)
        for i in range(1, len(someHash) + 1):
            if str(i) in someHash.keys():
                resultList += [someHash[str(i)]]
        #join the list together with a space in between
        temp = ' '
        result = temp.join(resultList)

        return result


