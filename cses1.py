num = int(input())
print(int(num), end=" ")

while(num != 1):
    if(num%2 == 0):
        num /= 2
    else:
        num = num*3 + 1
    print(int(num), end=" ")