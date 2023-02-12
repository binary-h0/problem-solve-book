# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import queue

def bfs_iterate(current_pos):
    que = queue.Queue()
    que.put((current_pos, 0))
    cnt = 0
    c = 0
    while not que.empty():
        c_p, count = que.get()
        if c_p == k:
            print(count)
            cnt += 1
            c = count
            break
        visited[c_p] = 1
        n_p = c_p - 1
        if 0 <= n_p:
            if visited[n_p] == 0:
                que.put((n_p, count + 1))
        n_p = c_p + 1
        if n_p <= 100000:
            if visited[n_p] == 0:
                que.put((n_p, count + 1))
        n_p = c_p * 2
        if n_p <= 150000:
            if visited[n_p] == 0:
                que.put((n_p, count + 1))

    while not que.empty():
        c_p, count = que.get()
        if c_p == k and count == c:
            cnt += 1
    print(cnt)



if __name__ == '__main__':
    visited = [0 for _ in range(200001)]
    n, k = map(int, input().split())
    if n > k:
        print(n - k)
        print(1)
    else:
        bfs_iterate(n)