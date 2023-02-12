# 자료구조, 해시를 사용한 집합과 맵, 분리 집합
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def find(x):
    global parent
    if x == parent[x]:
        return x
    else:
        parent_x = find(parent[x])
        parent[x] = parent_x
        return parent[x]
def union(x, y):
    global parent, number
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]

if __name__ == '__main__':
    for __ in range(int(input().rstrip())):
        parent = dict()
        number = dict()
        for _ in range(int(input().rstrip())):
            x, y = map(str, input().rstrip().split())
            if not x in parent:
                parent[x] = x
                number[x] = 1
            if not y in parent:
                parent[y] = y
                number[y] = 1
            union(x, y)
            print("%d\n" %number[find(x)])