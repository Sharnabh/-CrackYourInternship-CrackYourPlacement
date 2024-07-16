class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = max(nums)
        dup = [0] * (m+1)
        for i in nums:
            dup[i] += 1

        res = []
        for i in range(m+1):
            if(dup[i] == 2):
                res.append(i)

        return res