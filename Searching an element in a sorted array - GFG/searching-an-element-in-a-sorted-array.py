#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        if K in arr:
            return 1
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		ob=Solution()
		print(ob.searchInSorted(A,N,K))

# } Driver Code Ends