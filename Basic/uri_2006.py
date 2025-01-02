T = int(input())
p1 = list(map(int,input().split()))
count = 0

for i in p1:
    if i == T:
        count+=1

print(count)