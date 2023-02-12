# 누적합
input = __import__('sys').stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    lis = list(map(int, input().rstrip().split()))

    for i in range(1, n):
        lis[i] += lis[i - 1]

    for _ in range(m):
        s, e = map(int, input().rstrip().split())
        if s == 1:
            print(lis[e - 1])
        else:
            print(lis[e - 1] - lis[s - 2])