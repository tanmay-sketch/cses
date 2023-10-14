seq = input()

ans = 1
count = 0

start = 'A'

for char in seq:
    if(char == start):
        count += 1
        ans = max(count,ans)
    else:
        start = char
        count = 1

print(ans)
