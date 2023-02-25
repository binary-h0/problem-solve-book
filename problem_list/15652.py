import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().rstrip().split())
stack = []

def solve(s):
    if len(stack) == m:
        print(' '.join(map(str, stack)) + '\n')
        return
    for i in range(s, n + 1):
        stack.append(i)
        solve(i)
        stack.pop()

if __name__ == '__main__':
    solve(1)