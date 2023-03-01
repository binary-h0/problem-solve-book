import sys
input = sys.stdin.readline

def main():
    min_n, max_n = map(int, input().rstrip().split())
    answer = max_n - min_n + 1
    lis = [False for _ in range(answer)]
    for i in range(2, int(max_n**0.5 + 1)):
        square = i ** 2
        for j in range((((min_n - 1) // square) + 1) * square, max_n + 1, square):
            if not lis[j - min_n]:
                lis[j-min_n] = True
                answer -= 1
    print(answer)
main()