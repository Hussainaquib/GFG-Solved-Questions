#User function Template for python3
class Solution:
	def setBits(self, N):
		# code here
		a=bin(N)[2:]
		res1=[int(x) for x in str(a)]
		return res1.count(1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends