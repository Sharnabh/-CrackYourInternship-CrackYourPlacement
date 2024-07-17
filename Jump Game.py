class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = 0
        for i in nums:
            if j < 0:
                return False
            elif i > j:
                j = i
            j -= 1

        return True