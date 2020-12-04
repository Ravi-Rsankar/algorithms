# Brute force
def maxIndexDiff(arr, n):
    max = -1
    for i in range(0,n):
        j = n-1
        while j > i:
            # print("while loop: j-"+str(j)+" i: "+str(i))
            if arr[i] <= arr[j] and max < (j-i):
                max = j-i
            j-=1
    return max

# Using Binary search 
def alternateSol(v, n):
    maxFromEnd = [-38749432] * (n + 1)
    for i in range(n - 1, 0, -1):
        maxFromEnd[i] = max(maxFromEnd[i+1], v[i])
    result = 0
    print(maxFromEnd)
    print(v)
    for i in range(0, n):
        low = i + 1; high = n - 1; ans = i
        
        while (low <= high):
            mid = int((low + high) / 2)
            print("i: "+str(i) + " low: "+str(low)+ " high: "+str(high)+ " ans: "+str(ans)+ " mid: "+str(mid))
            if (v[i] <= maxFromEnd[mid]):
            
                # We store this as current
                # answer and look for further
                # larger number to the right side
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1;        

        # Keeping a track of the
        # maximum difference in indices
        result = max(result, ans - i)
        print(result)
        
    return result

# Using Merge sort
def finalSol(arr, n):
    minArr = [0 for i in range(n)]
    minArr[0] = arr[0]
    for i in range (1, n):
        minArr[i] = min(arr[i], minArr[i-1])
    maxArr = [0 for i in range(n)]
    maxArr[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        maxArr[i] = max(arr[i], maxArr[i+1])
    i, j, maxDiff = 0,0,0
    
    while i < len(minArr) and j < len(maxArr):
        if minArr[i] <= maxArr[j]:
            maxDiff = max(maxDiff, j-i)
            j+=1
        else:
            i+=1
    return maxDiff
    
arr = [34,8,10,3,2,80,30,33,1]
n = len(arr)
result = finalSol(arr, n)
print(result)
