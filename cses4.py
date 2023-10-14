size = input()
array = [int(x) for x in input().split()]

# list: 3 2 5 1 4
# swap: 0 1 2 4 1
# ans:  0 1 3 7 8

mx = 0
ans = 0

for i in range(0,len(array)):
    mx= max(array[i],mx)
    ans += mx - array[i]

print(ans)
