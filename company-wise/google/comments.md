# Comments

## Subarray with given sum

**References**:

[Subarray with given sum - YouTube](https://www.youtube.com/watch?v=Ofl4KgFhLsM)

[Find subarray with given sum | Set 1 (Nonnegative Numbers) - GeeksforGeeks](https://www.geeksforgeeks.org/find-subarray-with-given-sum/)

**Notes**: Have two pointers(Lazy and fast) sum up the lazy index value as it traverse and if the sum is greater than the given sum then subtract the index value of the lazy pointer.

## Maximum index

Explanation: [Given an array arr[\], find the maximum j - i such that arr[j] > arr[i] - GeeksforGeeks](https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/)

The above code throws time limit exceed error. Check the solution provided by geeksforgeeks on the question page. This solution makes a min and max array and finds the max difference using merge sort.

## Longest valid parentheses

Explanation: https://www.youtube.com/watch?v=r0-zx5ejdq0

## Jumping Numbers

Approach: Use the BFS or DFS approach to traverse all the jumping numbers. In BFS push each jumping number into the queue if its less than the given number. Perform this till the queue is empty