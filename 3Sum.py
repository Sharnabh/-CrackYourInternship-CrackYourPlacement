class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    trip = [nums[i], nums[l], nums[r]]
                    ans.append(trip)
                    while l < r and nums[l] == trip[1]:
                        l += 1
                    while l < r and nums[r] == trip[2]:
                        r -= 1
        return ans