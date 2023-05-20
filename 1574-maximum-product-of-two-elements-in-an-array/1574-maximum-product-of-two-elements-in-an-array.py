class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #can't you just sort it and take the last 2 indices and multiply them?

        numsSorted = sorted(nums)
        i = numsSorted[-1] - 1
        j = numsSorted[-2] - 1
        return i * j 