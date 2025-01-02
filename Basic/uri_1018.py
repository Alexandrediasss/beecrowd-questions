N = int(input())

print(N)

count100 = 0
count50 = 0
count20 = 0
count10 = 0
count5 = 0
count2 = 0
count1 = 0

while N >=100:
    N-=100
    count100+=1

while N >=50:
    N-=50
    count50+=1

while N >=20:
    N-=20
    count20+=1

while N >=10:
    N-=10
    count10+=1

while N >=5:
    N-=5
    count5+=1

while N >=2:
    N-=2
    count2+=1

while N >=1:
    N-=1
    count1+=1

print(f"{count100} nota(s) de R$ 100,00")
print(f"{count50} nota(s) de R$ 50,00")
print(f"{count20} nota(s) de R$ 20,00")
print(f"{count10} nota(s) de R$ 10,00")
print(f"{count5} nota(s) de R$ 5,00")
print(f"{count2} nota(s) de R$ 2,00")
print(f"{count1} nota(s) de R$ 1,00")