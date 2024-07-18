class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r = 0, len(h) -1
        max_area = 0
        while l < r:
            area = (r - l) * min(h[l], h[r])
            max_area = max(area, max_area)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1

        return max_area