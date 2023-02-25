# 자료구조, 문자열, 스택
import sys
input = sys.stdin.readline
print = sys.stdout.write
s = list(input().rstrip())
target = list(input().rstrip())

def solve():
    stack = []
    n = len(target)
    i = 0
    flag = False
    for c in s:
        if target[n-1] == c:
            stack.append(c)
            if target == stack[len(stack) - n:len(stack)]:
                for _ in range(n):
                    stack.pop()
        else:
            stack.append(c)
    if len(stack) == 0:
        print("FRULA")
    else:
        for i in stack:
            print(i)

if __name__ == '__main__':
    solve()