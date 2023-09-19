#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self, n):
        if n == 0:
            return 0
        
        # Initialize a position variable.
        position = 1
        
        # Iterate through the bits of n.
        while n > 0:
            # Check if the rightmost bit is set (i.e., it's 1).
            if n & 1 == 1:
                return position
            # Right shift n to check the next bit.
            n = n >> 1
            position += 1
        
        # If no set bit is found, return 0.
        return 0

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends