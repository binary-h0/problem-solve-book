# 자료구조, 스택
import sys
input = sys.stdin.readline

formation = ""
length = ""
check = []
is_legal = True

for _ in range(int(input())):
    # print(input())
    is_legal = True
    check = []
    length, formation = input().split()
    for i in range(int(length)):
        if formation[i] == '<':
            if len(check) == 0:
                is_legal = False
                break
            if check.pop() != '>':
                is_legal = False
                break
        else:
            check.append(formation[i])

    if len(check) != 0:
        is_legal = False

    if is_legal:
        print("legal")
    else:
        print("illegal")
