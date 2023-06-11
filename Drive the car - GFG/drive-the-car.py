#User function Template for python3

class Solution:
    def required(self, a, n, k):
        if max(a)>k:
            return max(a)-k
        else:
            return -1
                
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.required(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends