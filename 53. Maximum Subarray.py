class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = local_maxx = nums[0]

        for i in nums[1:]:
            local_maxx = max(i, i + local_maxx)

            maxx = max(local_maxx, maxx)

        return maxx


#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.


#solution is to use Kadene's Algo.
# Local_max[i] = max(nums[i] , nums[i] + local_max[i - 1)