class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # input/key is n
        # value is number of times n appears in nums
        someHash = {}

        for n in nums:
            if n not in someHash:
                someHash[n] = 1
            else:
                return True
                
        return False
        
