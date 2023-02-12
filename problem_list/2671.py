# 문자열, 정규표현식
import sys
import re
input = sys.stdin.readline

def solve(string):
    r = re.compile("(100+1+|01)+")
    if r.fullmatch(sound) == None:
        print("NOISE")
    else:
        print("SUBMARINE")

if __name__ == '__main__':
    sound = input().rstrip()
    solve(sound)