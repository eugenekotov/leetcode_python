class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resultIndex = 1
        for i in range(1, len(nums)):
            if not nums[i] == nums[i-1]:
                nums[resultIndex] = nums[i]
                resultIndex += 1

        return resultIndex


solution = Solution()
arg1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(arg1)
print(solution.removeDuplicates(arg1))
print(arg1)
