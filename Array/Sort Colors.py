class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        low = 0
        high = n-1
        i = 0
        while i <= high:
            if arr[i] == 0:
                arr[i], arr[low] = arr[low], arr[i]
                low += 1
            
            elif arr[i] == 2:
                arr[i], arr[high] = arr[high], arr[i]
                i -= 1
                high -= 1

            i += 1
                
            