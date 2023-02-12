s = input()
ans = [0 for _ in range(26)]
for i in range(len(s)):
    ans[ord(s[i]) - 97] += 1
print(*ans)