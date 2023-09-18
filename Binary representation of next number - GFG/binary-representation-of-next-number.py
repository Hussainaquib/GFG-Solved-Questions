#User function Template for python3
class Solution:
	def binaryNextNumber(self, S):
        x=int(S,2)+1
        return '{0:b}'.format(x)
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution();
		ans = ob.binaryNextNumber(S)
		print(ans)

# } Driver Code Ends