# 구현
import sys
if __name__ == '__main__':
    n = int(input())
    a = ['*' for _ in range(n)]
    for i in range(1, n, 2):
        a[i] = ' '
    b = ['*' for _ in range(n)]
    for i in range(0, n, 2):
        b[i] = ' '

    if n == 1:
        print("*")
    else:
        for _ in range(n):
            for i in range(len(a) - 1):
                print(a[i], end='')
            print(a[n-1])
            for i in range(len(b) - 1):
                print(b[i], end='')
            print(b[n-1])