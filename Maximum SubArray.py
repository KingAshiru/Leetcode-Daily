class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArray = subArraySum = nums[0]
        
        for num in nums[1:]:
            subArraySum = max(num, subArraySum + num)
            maxSubArray = max(maxSubArray, subArraySum)
            
        return maxSubArray
