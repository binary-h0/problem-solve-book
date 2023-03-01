import sys

def main():
    H, W = map(int, input().rstrip().split())
    graph = [list(input().rstrip()) for _ in range(H)]
    key_lis = set()
    for key in input().rstrip():
        if key == '0':
            break
        key_lis.add(chr(ord(key)-32))
    coords = []
    for

if __name__ == '__main__':
    for _ in range(int(input().rstrip())):
        main()