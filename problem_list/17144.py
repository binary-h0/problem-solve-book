import sys
input = sys.stdin.readline
R, C, T = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(R)]

def diffuse():
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    dust_coords = []
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                dust_coords.append((r, c, graph[r][c]))
    for r, c, w in dust_coords:
        d_w, count = w // 5, 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not ((0 <= nr < R) and (0 <= nc < C)):
                continue
            if graph[nr][nc] == -1:
                continue
            count += 1
            graph[nr][nc] += d_w
        graph[r][c] -= d_w * count

def aircleaning():
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    for k in range(R):
        if graph[k][0] == -1:
            i, r, c = 0, k-1, 0
            while True:
                nr, nc = r + dr[i], c + dc[i]
                if not ((0 <= nr <= k) and (0 <= nc < C)):
                    i = (i + 1) % 4
                    continue
                if (nr == k) and (nc == 0):
                    graph[r][c] = 0
                    break
                graph[r][c] = graph[nr][nc]
                r, c = nr, nc
            dr = [1, 0, -1, 0]
            i, r, c = 0, k + 2, 0
            while True:
                nr, nc = r + dr[i], c + dc[i]
                if not ((k+1 <= nr < R) and (0 <= nc < C)):
                    i = (i + 1) % 4
                    continue
                if (nr == k+1) and (nc == 0):
                    graph[r][c] = 0
                    break
                graph[r][c] = graph[nr][nc]
                r, c = nr, nc
            break

def simulate():
    diffuse()
    aircleaning()

if __name__ == '__main__':
    for _ in range(T):
        simulate()
    ans = 2
    for dusts in graph:
        ans += sum(dusts)
    print(ans)
# 3 3 1
# 0 30 7
# -1 10 0
# -1 0 20