import sys
input = sys.stdin.readline

def solve(s):
    stack = []
    isLaser = True
    answer = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            isLaser = True
        elif isLaser:
            stack.pop()
            answer += len(stack)
            isLaser = False
        else:
            stack.pop()
            answer += 1
    print(answer)

if __name__ == '__main__':
    string = input().rstrip()
    solve(string)