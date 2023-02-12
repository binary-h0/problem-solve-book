# 수학, 문자열, 그리디, 파싱
input = __import__('sys').stdin.readline

def solve():
    lis = s.split('-')
    ans = sum(list(map(int, lis[0].split('+'))))
    for i in range(1, len(lis)):
        ans -= sum(list(map(int, lis[i].split('+'))))
    print(ans)

if __name__ == '__main__':
    s = input().rstrip()
    solve()