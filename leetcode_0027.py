class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        resultIndex = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[resultIndex] = nums[i]
                resultIndex += 1
        return resultIndex


solution = Solution()
# args 1
arr1 = [3, 2, 2, 3]
val1 = 3
print(arr1)
print(val1)
print(solution.removeElement(arr1, val1))
print(arr1)

# args 1
arr1 = [0, 1, 2, 2, 3, 0, 4, 2]
val1 = 2
print(arr1)
print(val1)
print(solution.removeElement(arr1, val1))
print(arr1)
