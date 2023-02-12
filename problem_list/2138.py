import sys
input = sys.stdin.readline
n = int(input().rstrip())
def click(state, i):
    for idx in range(max(0, i - 1), min(i+2, n), 1):
        if state[idx] == '1':
            state[idx] = '0'
        else:
            state[idx] = '1'

def solve():
    state1 = list(i for i in input().rstrip())
    state2 = state1[:]
    resultState = list(i for i in input().rstrip())
    count1, count2 = 1, 0
    click(state1, 0)
    for i in range(1, n):
        if resultState[i - 1] != state1[i - 1]:
            click(state1, i)
            count1 += 1
        if resultState[i - 1] != state2[i - 1]:
            click(state2, i)
            count2 += 1
    if state1 == resultState and state2 == resultState:
        print(min(count1, count2))
    elif state1 == resultState:
        print(count1)
    elif state2 == resultState:
        print(count2)
    else:
        print(-1)

if __name__ == '__main__':
    solve()