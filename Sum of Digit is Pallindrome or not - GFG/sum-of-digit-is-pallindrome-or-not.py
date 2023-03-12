#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        sum = 0
        while(N > 0):
            sum += int(N % 10)
            N = int(N/10)
        res1 = [int(x) for x in str(sum)]
	    res1.reverse()
	    m = int("".join(map(str, res1)))
	    if sum==m:
	        return 1
        else:
            return 0
 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends