#User function Template for python3

import heapq
class Solution:
    def maxDiamonds(self, A, N, k):
        c=[]
        for i in A:
            heapq.heappush(c,-i)
        a=0
        while(k>0):
            x=-heapq.heappop(c)
            a+=x
            x=x//2
            heapq.heappush(c,-x)
            k-=1
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends