class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        count = 0
        for i in [0] + list(accumulate(nums)):
            count += sums[i-k]
            sums[i] += 1
        return count