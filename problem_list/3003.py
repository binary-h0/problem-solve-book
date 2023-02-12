# 수학, 구현, 사칙연산
chess = [1, 1, 2, 2, 2, 8]
lis = list(map(int, input().split()))
for i in range(6):
    chess[i] -= lis[i]
print(*chess)