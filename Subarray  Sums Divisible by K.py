class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_mod = 0
        res = 0

        mod_groups = [0] * k
        mod_groups[0] = 1

        for i in nums:
            prefix_mod = (prefix_mod + i % k + k) % k
            res += mod_groups[prefix_mod]
            mod_groups[prefix_mod] += 1

        return res