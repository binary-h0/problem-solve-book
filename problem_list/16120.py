import sys
input = sys.stdin.readline

def solve():
    s = input().rstrip()
    stack = []
    if s[-1] == 'A':
        print('NP')
        return
    for i in range(len(s) - 1):
        if s[i] == 'P':
            stack.append(s[i])
            continue
        if (len(stack) >= 2) and (s[i+1] == 'P'):
            stack.pop()
            stack.pop()
        else:
            print("NP")
            return
    if (len(stack) == 0) or (s == 'P'):
        print("PPAP")
    else:
        print("NP")

if __name__ == '__main__':
    solve()