class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
        'q','r','s','t','u','v','w','x','y', 'z']
        
        morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        hashAlph = {}
        for i in range(len(alphabet)):
            hashAlph[alphabet[i]] = morseAlphabet[i]

        transformations = []
        #transform every word
        for word in words:
            trans = ''
            #translates the word in morse
            for letter in word:
                trans += hashAlph[letter]

            #removes duplicates
            if trans not in transformations:
                transformations.append(trans)
            
        
        return(len(transformations))





        