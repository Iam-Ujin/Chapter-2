class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j = 0, 0
        n = len(nums) - 1
        while j <= n :
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            else:
                j += 1