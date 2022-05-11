class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        result = []
        a = defaultdict(int)
        for i in nums:
            a[i] += 1
        print(a)
        for i in nums:
            a[i] -= 1
            temp = 1
            for j in a.keys():
                if a[j] > 0:
                    temp *= j ** a[j] 
            result.append(temp)
            a[i] += 1
        return result

        # temp = 1
        # for i in nums[1::]:
        #     temp *= i
        # result.append(temp)
        # for i in range(1, len(nums)):
        #     new = nums[:i]
        #     if nums[i] == 0:
        #         temp = 1
        #         for i in nums[:i] + nums[i+1:]:
        #             temp *= i
        #     else:
        #         temp = temp//nums[i]
        #         # for i in new:
        #         #     temp *= i
        #         temp *= nums[i-1]
        #     result.append(temp)            
            