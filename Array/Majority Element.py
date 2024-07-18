class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        s = list(set(nums))
        maj = n//2
        for i in range(0, len(s)):
            c = nums.count(s[i])
            if c > maj:
                return s[i]