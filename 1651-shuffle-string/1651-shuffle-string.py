class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        '''
        Initial Thoughts:
        len of s and indices are guaranteed to be equal
        iterate thru range(len(indices)) and build a new str based on that
        '''

        result = ''
        for i in range(len(indices)):
            result += s[indices.index(i)]

        return result
