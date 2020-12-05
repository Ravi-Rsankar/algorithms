
def findLongestParantheses(string):
    stack = []
    stack.append(-1)
    result = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        else:
            if len(stack)!=0:
                stack.pop()
            if len(stack)!=0:
                result = max(result, i-stack[len(stack)-1])
            else:
                stack.append(i)
    return result
     
testcase = int(input())
for case in range(0, testcase):
    paran = input()
    length = findLongestParantheses(paran)
    print(length)
