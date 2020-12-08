from collections import Counter
arr = [18, 24,24, 21, 10, 29, 8, 10, 29, 18]
c = sorted(arr)
arr.sort()
print(arr)
x = Counter(sorted(arr))
result = []
for i in x.items():
    if i[1] < 2:
        result.append(str(i[0]))
print(" ".join(result))
