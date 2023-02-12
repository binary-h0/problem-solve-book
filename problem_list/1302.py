# 자료구조, 문자열, 정렬, 해시를 사용한 집합과 맵
import sys
input = sys.stdin.readline

books = dict()
for _ in range(int(input().rstrip())):
    book = input().rstrip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

maxBookCount = max(books.values())
books = dict(sorted(books.items(), key=lambda x : x[0]))
for key in books.keys():
    if maxBookCount == books[key]:
        print(key)
        break