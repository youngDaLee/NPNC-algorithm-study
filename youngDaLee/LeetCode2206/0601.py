class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSums = [0] * len(nums)
        for i in range(len(nums)):
            runningSums[i] = runningSums[i-1] + nums[i]

        return runningSums