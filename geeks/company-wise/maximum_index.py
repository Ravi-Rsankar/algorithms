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


def alternateSol(v, n):
    maxFromEnd = [-38749432] * (n + 1)
    for i in range(n - 1, 0, -1):
        maxFromEnd[i] = max(maxFromEnd[i + 1], v[i])
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

arr = [34,8,10,3,2,80,30,33,1]
n = len(arr)
result = alternateSol(arr, n)
print(result)
