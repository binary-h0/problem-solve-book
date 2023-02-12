# 분할 정복, 재귀
import sys
input = sys.stdin.readline

def solve(lr, hr, lc, hc):
    global maxIndex, minIndex
    r_pivot, c_pivot = (lr + hr) >> 1, (lc + hc) >> 1
    if r_pivot <= r:
        minIndex = (minIndex + maxIndex) >> 1
    else:
        maxIndex = (minIndex + maxIndex) >> 1
    if c_pivot <= c:
        minIndex = (minIndex + maxIndex) >> 1
    else:
        maxIndex = (minIndex + maxIndex) >> 1

    if r_pivot == r and c_pivot == c:
        return minIndex
    else:
        if r_pivot <= r:
            if c_pivot <= c:
                return solve(r_pivot, hr, c_pivot, hc)
            else:
                return solve(r_pivot, hr, lc, c_pivot)
        else:
            if c_pivot <= c:
                return solve(lr, r_pivot, c_pivot, hc)
            else:
                return solve(lr, r_pivot, lc, c_pivot)



if __name__ == '__main__':
    n, r, c = map(int, input().rstrip().split())
    length = 2 ** n
    maxIndex = 2 ** (n*2)
    minIndex = 0

    print(solve(0, length, 0, length))