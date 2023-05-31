#User function Template for python3
class Solution:
    def isPowerOfAnother (ob,X,Y):
        for i in range(Y):
            if X**i==Y:
                return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        X,Y=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.isPowerOfAnother(X,Y))
# } Driver Code Ends