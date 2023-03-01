# 자료구조, 세그먼트 트리
import sys
import math
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def init_segment(idx, s, e, seg, arr):
    if s == e:
        seg[idx] = (arr[s], arr[s])
        return seg[idx]
    mid = (s + e) // 2
    l = init_segment(idx * 2, s, mid, seg, arr)
    r = init_segment(idx * 2 + 1, mid + 1, e, seg, arr)
    seg[idx] = (min(l[0], r[0]), max(l[1], r[1]))
    return seg[idx]
def find(s, e, idx, seg, ts, te):
    if e < ts or te < s:
        return (1000000000, 0)
    mid = (s + e) // 2
    if ts <= s and e <= te:
        return seg[idx]
    else:
        l = find(s, mid, idx * 2, seg, ts, te)
        r = find(mid + 1, e, idx * 2 + 1, seg, ts, te)
        return (min(l[0], r[0]), max(l[1], r[1]))
def main():
    N, M= map(int, input().rstrip().split())
    lis = [int(input().rstrip()) for _ in range(N)]
    h = math.ceil(math.log2(N)) + 1
    node_num = 1 << h
    segment_tree = [0 for _ in range(node_num)]
    init_segment(1, 0, len(lis) - 1, segment_tree, lis)
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        print(*find(0, len(lis) - 1, 1, segment_tree, a-1, b-1))
# main()
# 다른 풀이
import sys

input = sys.stdin.readline
flush = sys.stdout.flush
def build():
    for i in reversed(range(1, n)):
        segm[i] = min(segm[2*i], segm[2*i + 1])
        segM[i] = max(segM[2*i], segM[2*i + 1])
    return

def query(l, r):
    l += n
    r += n
    m, M = 10**9 + 1, 0
    while l < r:
        if l & 1:
            if segm[l] < m:
                m = segm[l]
            if segM[l] > M:
                M = segM[l]
            l += 1
        if r & 1:
            r -= 1
            if segm[r] < m:
                m = segm[r]
            if segM[r] > M:
                M = segM[r]
        l >>= 1
        r >>= 1
    return m, M

n, m = map(int, input().split())
segm = [0] * n
segM = [0] * n
for _ in range(n):
    x = int(input())
    segm.append(x)
    segM.append(x)

build()
print(segm)
print(segM)
for _ in range(m):
    a, b = map(int, input().split())
    print(*query(a - 1, b))
