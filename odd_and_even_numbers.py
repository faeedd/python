n = input()
odd = set()
even = set()
for ch in n:
    if int(ch) % 2 == 0:
        even.add(ch)
    else:
        odd.add(ch)
print(*sorted(even))
print(*sorted(odd))
