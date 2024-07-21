#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, t):
        #code here
        if len(s) < len(t):
            return -1
        
        map = [0] * 128
        count = len(t)
        start = 0
        min_len = float('inf')
        min_start = 0
        
        for c in t:
            map[ord(c)] += 1
        
        for end in range(len(s)):
            if map[ord(s[end])] > 0:
                count -= 1
            map[ord(s[end])] -= 1
            
            while count == 0:
                if end - start + 1 < min_len:
                    min_start = start
                    min_len = end - start + 1
                
                map[ord(s[start])] += 1
                if map[ord(s[start])] > 0:
                    count += 1
                start += 1
        
        return -1 if min_len == float('inf') else s[min_start:min_start + min_len]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends