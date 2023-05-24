class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Make nums2 into a hashMap where the key is the index and whose value is value
        nums2Dict = {}

        for i in range(len(nums2)):
            nums2Dict[i] = nums2[i]

        result = []

        for num in nums1:
            #num in nums1 will always find a number in nums2 as a subset
            for i in range(len(nums2Dict.keys())):
                #Find the subset
                if num == nums2Dict[i]:    
                    #if its last element
                    if i + 1 >= len(nums2Dict.keys()):
                        result += [-1]
                        break

                    #else check the remaining values
                    else:
                        for j in range(i, len(nums2Dict.keys())):
                            if j + 1 >= len(nums2Dict.keys()):
                                result += [-1]
                                break

                            if num < nums2Dict[j + 1]:
                                result += [nums2Dict[j + 1]]
                                break





        return result
                

