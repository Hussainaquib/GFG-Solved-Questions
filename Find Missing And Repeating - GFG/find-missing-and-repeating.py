#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        repeat=sum(arr)-sum(set(arr))
        a=list(set(arr))
        a.sort()
        if ((a[-1] * (a[-1] + 1)) // 2)-(sum(a))==0:
            missing = a[-1]+1
        else:
            missing=((a[-1] * (a[-1] + 1)) // 2)-(sum(a))
        return [repeat, missing]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends