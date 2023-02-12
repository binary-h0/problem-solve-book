# 수학, 다이나믹 프로그래밍

ret = 4
f1 = 1
f2 = 1
for _ in range(int(input()) - 1):
    f1, f2 = f2, f1 + f2
    ret += f1 * 2
print(ret)