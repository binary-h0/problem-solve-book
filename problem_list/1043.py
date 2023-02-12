# 자료구조, 그래프 이론, 그래프 탐색, 분리 집합
import sys
from collections import deque
input = sys.stdin.readline
que = deque()

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    answer = m
    knowns = list(map(int, input().rstrip().split()))
    knowns_memory = [0 for _ in range(51)]
    for i in range(knowns[0]):
        knowns_memory[knowns[i+1]] = 1
        que.append(knowns[i+1])
    partys = [set(list(map(int, input().rstrip().split()))[1:]) for _ in range(m)]
    partys_memory = [0 for _ in range(51)]

    while que:
        known = que.popleft()
        for i in range(len(partys)):
            party = partys[i]
            if partys_memory[i]:
                continue
            if known in party:
                partys_memory[i] = 1
                for people in party:
                    if knowns_memory[people]:
                        continue
                    knowns_memory[people] = 1
                    que.append(people)
    print(answer - sum(partys_memory))