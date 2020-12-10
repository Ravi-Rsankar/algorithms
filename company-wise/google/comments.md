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

Use stack to solve this. keep pushing the brackets and when u get the `)` pop the stack if the stack has any `(`. To make sure that the stack is not empty add a constant say `-1` while initializing the stack

Explanation: https://www.youtube.com/watch?v=r0-zx5ejdq0

## Jumping Numbers

Approach: Use the BFS or DFS approach to traverse all the jumping numbers. In BFS push each jumping number into the queue if its less than the given number. Perform this till the queue is empty

> While checking if list is empty, always use `list == []` instead of using `len(list)==0`. The later takes more time than the former and I got a time exceeded error when I used the `len()` function to check. 
>

## Connect nodes at same level

For a given tree, the left child of the root need to be connected to the right child. At any given level, all the nodes needs to be connected and the last node in each level will be pointing to null. 

A specific property `next` will be provided to keep track of the next node. Apart from this variable the node will have `left` and `right` properties. The `next` should be made to point to the next node on the same level.

For any given node, check if the node is not null and the node has a level below. While it has a level below then connect all the nodes in level below.  To do so, have a `pointer`(initialize a `node` from the `root`) which keeps moving right once the child nodes are connected. The  `next` of the `left` node will be pointing to the `right` node. Here there is a special case to be handled by the pointer when it comes to the last node in a level. Since the last node points to null, its `next` need not have to be updated and it remains `null`. So check if the `next` of a node is null and then connect the right node. If the `next` of the current node is not null, then `next` of the `right` node will be `left` node of the current node's `next`. Follow the [Video](https://www.youtube.com/watch?v=bmjAiDsIDas) to get more clarity. 

Once the nodes in the immediate next level is connected then move the pointer to the left of the root making it the root for the next iteration. 

The above approach gave wrong output for certain cases. On checking the solution in [geeksforgeeks](https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1), the nodes are right away pushed into a list and while the list is not empty, loop through the list and check if the element is the last node in the list. If not then assign the next element i.e., `list[1]` as the `next` of the current node. 

Check if the node has left and right child. If yes then push them to the list. At the end pop the current element `pop(0)` from the list. 

## Count BST nodes within a given range

Three check needs to be performed. 

1. If the data is within the range of the low and high value, then increment 1 and recur for both `right` and `left` node.
2. If the data is greater than the high, then recur for the `left` child 
3. If the data is less than the low, then recur for the `right` child.

Optionally to improve the efficiency, check if the data is equal to high and low values. This mean the low and high are same. If it is then return 1.

The count will be incremented on the first case where the recursion for `right` and `left` happens before incrementing thus returning sum of `1 + recursion of right + recursion of left`. 