n = int(input())
a = set()
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        a.add(i)
        a.add(n // i)
print(*sorted(a))
