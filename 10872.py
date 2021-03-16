i = int(input())

if i == 0:
    print(1)
else:
    f = 1
    for k in range(1, i + 1):
        f = f * i
    print(f)

