N = 50000

print("Start array")

a = []
for i in range(1, N):
    # i-1 lookups
    # summation 0 + 1 + 2 + ... + N-1
    # N * (N - 1) / 2
    if  i not in a:
        a.append(i)
print("End array", len(a))


print("Start set")
s = set()
for i in range(1, N):
    # 1 + 1 + ...
    s.add(i)

print("End set", len(s))

print("Start dict")
d = {}
for i in range(1, N):
    d[i] = True

print("End dict", len(d))