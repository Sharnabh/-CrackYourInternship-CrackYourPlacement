from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        # code here 
        ans = list(sorted(set(permutations(arr))))
        return ans