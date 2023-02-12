# 구현
n = input()
lis = [0 for _ in range(10)]
for i in range(len(n)):
    lis[int(n[i])] += 1
lis[9] += lis[6]
lis[6] = 0
if lis[9] % 2 == 0:
    lis[9] /= 2
else:
    lis[9] = (lis[9] + 1) / 2

print(int(max(lis)))