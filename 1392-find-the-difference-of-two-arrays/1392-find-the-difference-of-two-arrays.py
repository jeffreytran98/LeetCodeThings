class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = [number for number in nums1 if number not in nums2]
        ans2 = [number for number in nums2 if number not in nums1]
        
        return [set(ans1), set(ans2)]