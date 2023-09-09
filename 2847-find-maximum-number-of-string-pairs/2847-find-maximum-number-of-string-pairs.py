class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        counter = 0 
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                #if first letter is the same as second letter of the next word
                #and if second letter is same as first letter of the next word
                if words[i][0] == words[j][1] and words[i][1] == words[j][0]:
                    counter += 1 
        return counter