#User function Template for python3

def findElement( arr, n):
    
    ans=-1

    mx=arr[0]

    for i in range(1,n):

        if arr[i]<mx:

            ans=-1

        elif arr[i]>=mx:

            if ans==-1 and i!=n-1:

                ans=arr[i]

            mx=arr[i]

    return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends