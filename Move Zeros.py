class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur = lastNonZero = 0
        while cur < len(nums):
            if nums[cur] != 0:
                nums[lastNonZero], nums[cur] = nums[cur], nums[lastNonZero]
                lastNonZero += 1
            cur += 1
