#User function Template for python3

class Solution: 
    def select(self, arr, i):
        minIndex = i
        for i in range(minIndex, len(arr)):
            if arr[i] < arr[minIndex]:
                minIndex = i
        return minIndex
    
    def selectionSort(self, arr, n):
        for i in range(n):
            minValue = self.select(arr, i)
            arr[i], arr[minValue] = arr[minValue], arr[i]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
        

