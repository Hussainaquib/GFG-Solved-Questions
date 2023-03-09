# Return true if str is binary, else false
def isBinary(str):
    if(str.count('0')+str.count('1')==len(str)):
        return 1
    else:
        return 0
    #code here


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends