n = int(input())
line2 = sorted([int(x) for x in input().split()])
nums = [x for x in range(1,n+1)]

missing = 0

for i in range(len(nums)):
    if (i == (len(line2)-1)) and (nums[-1] != line2[-1]):
        missing = n
        break
    if(nums[i] != line2[i]):
        missing = nums[i]
        break


print(missing)