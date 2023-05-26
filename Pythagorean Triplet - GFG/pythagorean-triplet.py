#User function Template for python3
class Solution:

	def checkTriplet(self,arr, n):
	    squared_arr = [x**2 for x in arr]
        squared_arr.sort()

        n = len(squared_arr)
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if squared_arr[left] + squared_arr[right] == squared_arr[i]:
                    return True
                elif squared_arr[left] + squared_arr[right] < squared_arr[i]:
                    left += 1
                else:
                    right -= 1

        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends