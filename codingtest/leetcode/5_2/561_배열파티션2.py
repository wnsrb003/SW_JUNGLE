class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_n = 0
        for i in range(0,len(nums)-1,2):
            max_n += min(nums[i], nums[i+1])
        return (max_n)