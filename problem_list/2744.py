# 문자열, 구현

s = input()
for i in range(len(s) - 1):
    print(s[i].upper(), end='') if s[i].islower() else print(s[i].lower(), end='')
print(s[-1].upper()) if s[i].islower() else print(s[-1].lower())