# 분할 정복, 재귀
input = __import__('sys').stdin.readline

def solve(n, x, y):
    global graph
    if n == 1:
        return graph[x][y], str(graph[x][y])
    a1, s1 = solve(n // 2, x, y)
    a2, s2 = solve(n // 2, x, y + (n >> 1))
    a3, s3 = solve(n // 2, x + (n >> 1), y)
    a4, s4 = solve(n // 2, x + (n >> 1), y + (n >> 1))
    if (a1 + a2 + a3 + a4) == 4:
        return 1, "1"
    elif (a1 + a2 + a3 + a4) == 0:
        return 0, "0"
    else:
        return 5, "(" + s1 + s2 + s3 + s4 + ")"

if __name__ == '__main__':
    n = int(input().rstrip())
    graph = [list(map(int, input().rstrip())) for _ in range(n)]
    print(solve(n, 0, 0)[1])
