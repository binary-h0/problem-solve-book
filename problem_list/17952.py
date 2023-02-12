# 구현, 자료구조, 스택
import sys
input = sys.stdin.readline

score = 0
work = []
stack = []
for _ in range(int(input())):
    lis = list(map(int, input().split()))
    if lis[0]:
        if lis[2] == 1:
            score += lis[1]
        else:
            stack.append([lis[1], lis[2] - 1])
    else:
        if len(stack) == 0:
            continue
        work = stack.pop()
        if work[1] == 1:
            score += work[0]
        else:
            stack.append([work[0], work[1] - 1])
    # print(stack)
print(score)
