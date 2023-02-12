# # 브루트 포스
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# def solve():
#     global n, case2, buttons
#     n = str(n)
#     que = deque()
#     buttons.sort(key=lambda x: abs(x - int(n[0])))
#     if len(buttons) == 1:
#         que.append(buttons[0])
#     else:
#         if len(buttons) == 2:
#             que.append(buttons[0])
#             que.append(buttons[1])
#         else:
#             que.append(buttons[0])
#             que.append(buttons[1])
#             que.append(buttons[2])
#     for i in range(1, len(n)):
#         slice_n = int(n[:i+1])
#         for _ in range(len(que)):
#             s = str(que.popleft())
#             lis = []
#             for b in buttons:
#                 tmp = int(s + str(b))
#                 lis.append(tmp)
#             lis.sort(key=lambda x:abs(x - int(slice_n)))
#             que.append(lis[0])
#
#     s = str(que.popleft())
#     que.append(int(s))
#     lis = []
#     for b in buttons:
#         tmp = int(s + str(b))
#         lis.append(tmp)
#     lis.sort(key=lambda x: abs(x - int(n)))
#     que.append(lis[0])
#     que = list(que)
#     if len(s) != 1:
#         s = s[:len(s) - 1]
#         que.append(int(s))
#
#     s = ""
#     for _ in range(len(n) - 1):
#         s += str(max(buttons))
#     if len(n) > 1:
#         que.append(int(s))
#
#     buttons.sort()
#     s = ""
#     if buttons[0] == 0 and len(buttons) > 1:
#         s += str(buttons[1])
#     for _ in range(len(n)):
#         s += str(buttons[0])
#     que.append(int(s))
#     ans = []
#     for i in que:
#         ans.append(abs(int(n) - i) + len(str(i)))
#     case2 = min(ans)
#
#
# if __name__ == '__main__':
#     currentChannel = 100
#     buttons = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#     n = int(input().rstrip())
#     m = int(input().rstrip())
#     if m == 0:
#         jamButton = set([])
#     else:
#         jamButton = set(map(int, input().rstrip().split()))
#     buttons.difference_update(jamButton)
#     buttons = list(buttons)
#     case1 = abs(currentChannel - n)
#     case2 = 0
#     if len(buttons) != 0:
#         solve()
#         if case1 < case2:
#             print(case1)
#         else:
#             print(case2)
#     else:
#         print(case1)
#

import sys

s = sys.stdin.readline

N = int(s())
int(s())
wrong = list(map(int, s().split()))


def check(num):  # 제일 가까우면서 직접 누를 수 있는 번호 찾기
    for e in str(num):
        if int(e) in wrong:
            return False
    return True


def count():
	up = N
	down = N
	select_and_up = 0xFFFFFFFF
	select_and_down = 0xFFFFFFFF
	only_move = abs(N-100)
	while up != 100 and down != 100:
		if check(down):
			select_and_down = len(str(down)) + abs(N-down)
			break
		if check(up):
			select_and_up = len(str(up)) + abs(N-up)
			break
		up += 1
		if down > 0:
			down -= 1
	return min([select_and_up, select_and_down, only_move])

print(count())