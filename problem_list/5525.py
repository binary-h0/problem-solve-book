input = __import__('sys').stdin.readline

def solve():
    i = 0
    ans = 0
    oiCount = 0
    while i < m - 2:
        if s[i] == 'I':
            if s[i+1] == 'O' and s[i+2] == 'I':
                oiCount += 1
                i += 1
            else:
                oiCount = 0
            if oiCount >= n:
                ans += 1
        i += 1
    return ans

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    s = input().rstrip()
    print(solve())