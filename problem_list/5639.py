# 그래프 이론, 그래프 탐색, 트리, 재귀
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def solve(lis, s, e):
    if s > e:
        return
    m = e + 1
    for i in range(s + 1, e + 1):
        if lis[s] < lis[i]:
            m = i
            break
    solve(lis, s + 1, m - 1)
    solve(lis, m, e)
    print(lis[s])
def main():
    lis = []
    while 1:
        try:
            lis.append(int(input().rstrip()))
        except:
            break
    solve(lis, 0, len(lis) - 1)
main()