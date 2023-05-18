class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Initial thought is to create a HashMap and return the largest value
        someHash = {}
        for number in nums:
            if number not in someHash:
                someHash[number] = 1
            else:
                someHash[number] += 1

        #Largest value has been obtained, but you want the Key to this Value
        resultValue = max(someHash.values())
        for key in someHash:
            if someHash[key] == resultValue:
                return key
