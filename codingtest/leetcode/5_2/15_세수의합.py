class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        import itertools as i 
        nums.sort()
        result = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                else:
                    if nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    elif nums[i] + nums[left] + nums[right] < 0:
                        left += 1
        set_result = set()
        return list(set((map(tuple, result))))
        