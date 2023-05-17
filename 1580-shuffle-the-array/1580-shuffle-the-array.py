class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        resultList = []

        yNums = nums[n:]

        for i in range(n):
            resultList.append(nums[i])
            resultList.append(yNums[i])
        return resultList

        '''
        This is my old solution from idk how long ago
        final = []
        for i in range(len(nums)):
            if (i+n) >= len(nums):
                break
            final.append(nums[i])
            final.append(nums[i+n])

        return final

        '''