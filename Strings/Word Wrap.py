#User function Template for python3

import sys

class Solution:
    
    # Python program for the above approach
    def square(self, n) : 
    	return n * n 
    
    def solveWordWrapUtil(self, words, n, length,
    					wordIndex, remLength, memo) :
    
    	# base case for last word
    	if (wordIndex == n - 1) :
    		memo[wordIndex][remLength] = 0 if (words[wordIndex] < remLength) else square(remLength) 
    		return memo[wordIndex][remLength]
    	
    
    	currWord = words[wordIndex]
    	# if word can fit in the remaining line
    	if (currWord < remLength) :
    		return min(solveWordWrapUsingMemo(
    					words, n, length, wordIndex + 1,
    					remLength - currWord if (remLength == length) else remLength - currWord - 1,
    					memo),
    
    				square(remLength)
    					+ solveWordWrapUsingMemo(
    						words, n, length, wordIndex + 1,
    						length - currWord, memo))
    	
    	else :
    		# if word is kept on next line
    		return (square(remLength)
    			+ solveWordWrapUsingMemo(
    				words, n, length, wordIndex + 1,
    				length - currWord, memo))
    	
    def solveWordWrapUsingMemo(self, words, n, length,
    						wordIndex, remLength, memo) :
    								
    	if (memo[wordIndex][remLength] != -1) :
    		return memo[wordIndex][remLength]
    	
    	memo[wordIndex][remLength] = (solveWordWrapUtil(
    		words, n, length, wordIndex, remLength, memo))
    	return memo[wordIndex][remLength]
    
	def solveWordWrap(self, nums, k):
		#Code here
		n = len(nums)
        memo = [[10]* (k + 1)]* n
	    return Solution.solveWordWrapUsingMemo(nums, n, k, 0, k, memo)
		               
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		k = int(input())
		obj = Solution()
		ans = obj.solveWordWrap(nums, k)
		print(ans)


# } Driver Code Ends