class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for sentence in sentences:
            lengthCurrSentence = len(sentence.split(" "))
            if lengthCurrSentence >= result:
                result = lengthCurrSentence
        
        return result
