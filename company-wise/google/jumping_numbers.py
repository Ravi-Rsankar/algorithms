
class Queue:
    def __init__(self):
        self.lst = []
    def isEmpty(self):
        return self.lst == []
    def enqueue(self, item):
        self.lst.append(item)
    def dequeue(self):
        return self.lst.pop(0)

def printJumpingNumbers(x, num):
    seq = []
    q = Queue()
    q.enqueue(x)
    while not q.isEmpty():
        i = q.dequeue()
        if i <= num:
            seq.append(i)
            # print(str(i), end=" ")
            last_digit = i % 10
            if last_digit == 0:
                q.enqueue((i * 10) + (last_digit + 1))
            elif last_digit == 9:
                q.enqueue( (i * 10) + (last_digit - 1))
            else:
                q.enqueue((i * 10) + (last_digit + 1))
                q.enqueue((i * 10) + (last_digit - 1))
    return seq


testcase = int(input())
for case in range(0, testcase):
    num = int(input())
    output = [0]
    # print(str(0), end=" ")
    for x in range(1, 10):
        seq = printJumpingNumbers(x, num)
        output = output + seq
    print(" ".join(str(i) for i in sorted(output)))