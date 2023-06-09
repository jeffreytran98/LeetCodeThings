class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setNums1 = set(nums1)
        setNums2 = set(nums2)

        ans1 = [number for number in setNums1 if number not in setNums2]
        ans2 = [number for number in setNums2 if number not in setNums1]
        
        return [ans1, ans2]