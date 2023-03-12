#User function Template for python3

class Solution:
	def is_palindrome(self, n):
	    res1 = [int(x) for x in str(n)]
	    res1.reverse()
	    m = int("".join(map(str, res1)))
	    if n==m:
	        return "Yes"
        else:
            return "No"
	    
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends