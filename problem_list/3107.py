import sys
input = sys.stdin.readline
s = input().rstrip()

def solve():
    token_lis = s.split(':')
    for i in range(len(token_lis)-1):
        if (token_lis[i] == '') and (token_lis[i+1] == ''):
            token_lis.pop(i)
    n = len(token_lis)
    count = 0
    for i in range(8):
        if token_lis[i] == '':
            zeros = (8 - count) - (n - 1 - count)
            for _ in range(zeros-1):
                token_lis.insert(i+1, '')
            break
        count += 1
    ret = ""
    for i in range(7):
        ret += "0" * (4 - len(token_lis[i])) + token_lis[i] + ':'
    ret += "0" * (4 - len(token_lis[7])) + token_lis[7]
    print(ret)

if __name__ == '__main__':
    solve()