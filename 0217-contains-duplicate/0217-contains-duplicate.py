class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # input/key is n
        # value is number of times n appears in nums
        someHash = {}

        for n in nums:
            if n not in someHash:
                someHash[n] = 1
            else:
                #If n is not in someHash, it implies there is more than 1 n
                return True

        #if it finishes, then all elements are distinct
        return False
        
