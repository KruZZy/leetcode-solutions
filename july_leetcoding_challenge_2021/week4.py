class Solution(object):
    def partitionDisjoint(self, nums):
        left_max = nums[0]
        last_max = nums[0]
        cut = 0

        for i in range(1, len(nums)):
            if nums[i] < left_max: 
                cut = i 
                left_max = last_max 
            else:
                last_max = max(nums[i], last_max)

        return cut+1 

