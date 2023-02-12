# 구현, 브루트포스. 백트래킹
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = list(list(map(int, input().rstrip().split())) for _ in range(n))
house_coords = []
chicken_coords = []
distChickenToHouse = {}

def parseCoord():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                house_coords.append( [i, j] )
            elif graph[i][j] == 2:
                chicken_coords.append( [i, j] )

def calcDist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def solve():
    answer = 10 ** 9
    for comb in combinations(chicken_coords, m):
        comb_total_dist = 0
        for house_coord in house_coords:
            dist = 999
            r1, c1 = house_coord[0], house_coord[1]
            for chicken_coord in comb:
                r2, c2 = chicken_coord[0], chicken_coord[1]
                calc_dist = calcDist(r1, c1, r2, c2)
                if calc_dist < dist:
                    dist = calc_dist
            comb_total_dist += dist
            if comb_total_dist > answer:
                break
        if comb_total_dist < answer:
            answer = comb_total_dist
    print(answer)

if __name__ == '__main__':
    parseCoord()
    solve()