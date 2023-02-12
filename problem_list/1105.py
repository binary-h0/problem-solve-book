import sys
input = sys.stdin.readline
l, r = input().rstrip().split()

def solve():
    if len(l) != len(r):
        print(0)
        return
    count = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                count += 1
        else:
            break
    print(count)

if __name__ == '__main__':
    solve()