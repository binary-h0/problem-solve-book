n = int(input())

def checkNum(num):
    global twoCount, fiveCount
    while num % 5 == 0:
        num //= 5
        fiveCount += 1
    while num % 2 == 0:
        num //= 2
        twoCount += 1

if __name__ == '__main__':
    twoCount = 0
    fiveCount = 0
    for i in range(n , 0, -1):
        checkNum(i)

    print(min(twoCount, fiveCount))