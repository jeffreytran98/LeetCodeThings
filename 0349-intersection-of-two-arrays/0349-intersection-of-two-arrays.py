class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashTable = {}
        for num in nums1:
            if num in nums2:
                if num not in hashTable:
                    hashTable[num] = 1
                else:
                    hashTable[num] += 1

        return hashTable.keys()
        
