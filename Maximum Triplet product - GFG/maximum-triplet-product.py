#User function Template for python3

class Solution:
    def maxTripletProduct (self, arr,  n): 
        arr.sort()
        x = sum(1 for i in arr if i >= 0 )
        y = len(arr)-x
        b = arr[-1]*arr[-2]*arr[-3]
        a = arr[0]*arr[1]*arr[-1]
        if len(arr)==x:
            return b
        elif y>=2:
            if a>b:
                return a
            else:
                return b
        else:
            return b
        #Complete the function



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletProduct(arr, n)
    print(res)
# } Driver Code Ends