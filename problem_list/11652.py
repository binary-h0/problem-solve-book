# 자료구조, 정렬, 해시를 사용한 집합과 맵

cards = dict()
for _ in range(int(input())):
    c = input()
    if c in cards:
        cards[c] += 1
    else:
        cards[c] = 1

maxValue = max(cards.values())
flag = True
maxCard = 0
for key in cards.keys():
    if cards[key] == maxValue and flag:
        maxCard = int(key)
        flag = False
    elif cards[key] == maxValue and int(key) < maxCard:
        maxCard = int(key)
print(maxCard)