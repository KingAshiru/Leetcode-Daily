class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        windowStart = 0
        sum_ = 0.0
        maxSum = float("-inf")
        
        for windowEnd in range(len(nums)):
            sum_ += nums[windowEnd]
            if windowEnd >= k - 1:
                maxSum = max(maxSum, sum_)
                sum_ -= nums[windowStart]
                windowStart += 1
        return maxSum / k
