import sys
input = sys.stdin.readline

def solve(towers):
    n = len(towers)
    answer = [0 for _ in range(n)]
    stack = []
    tower_r = towers.pop()
    while towers:
        n -= 1
        tower_l = towers.pop()
        if tower_l < tower_r:
            stack.append((tower_r, n))
            tower_r = tower_l
        else:
            answer[n] = n
            while stack:
                t, i = stack.pop()
                if t <= tower_l:
                    answer[i] = n
                else:
                    stack.append((t, i))
                    break
            tower_r = tower_l
    print(*answer)

if __name__ == '__main__':
    n = int(input().rstrip())
    towers = list(map(int, input().rstrip().split()))
    solve(towers)