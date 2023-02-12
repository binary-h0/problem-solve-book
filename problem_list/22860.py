# 구현, 자료구조, 문자열, 해시를 사용한 집합과 맵
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

directory = dict()
n, m = map(int, input().rstrip().split())
fileSet = set()
fileCount = 0

for _ in range(n + m):
    p, f, isFolder = map(str, input().rstrip().split())

    if isFolder == '1':
        if p in directory:
            directory[p]["folder"].add(f)
            directory[f] = {"folder": set(), "file": set()}
        else:
            directory[p] = {"folder":set(), "file":set()}
            directory[p]["folder"].add(f)
            directory[f] = {"folder":set(), "file":set()}
    else:
        directory[p]["file"].add(f)
# print(directory)
def solve(folder):
    global fileCount
    for f in directory[folder]["folder"]:
        solve(f)
    for file in directory[folder]["file"]:
        fileSet.add(file)
        fileCount += 1
    return

for _ in range(int(input().rstrip())):
    fileSet.clear()
    fileCount = 0
    query = list(input().rstrip().split('/'))
    solve(query[-1])
    print(len(fileSet), fileCount)

