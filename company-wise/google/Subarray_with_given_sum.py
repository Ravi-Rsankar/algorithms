'''
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum.
The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.
'''
string = "135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134"

arr = [int(x) for x in string.split()]
s = 468
# print(len(arr))
print(arr[36])


def subarray(s, arr):
    sum = arr[0]
    i = 0
    j = 1
    # Loop through the fast pointer so as to end the loop once the length of array is reached.
    while j <= len(arr):
        # If sum is greater the s then subtract the starting value
        while sum > s:
            sum = sum - arr[i]
            i += 1
            print("Sum greater: sum: "+str(sum)+" i: "+str(i) + " j: "+str(j))
        # Return if values are same
        if sum == s:
            return str(i+1) + " " + str(j)
        # Sum up all the values in the list
        if j < len(arr):
            sum = sum + arr[j]
            print("Summing up the values. Sum: "+str(sum))
        j += 1
    return -1


res = subarray(s, arr)
print(res)
# testcases = int(input())
# for i in range(0, testcases):
#     inp = [int(x) for x in input().split()]
#     arr = [int(x) for x in input().split()]
#     res = subarray(inp[1], arr)
#     print(res)
