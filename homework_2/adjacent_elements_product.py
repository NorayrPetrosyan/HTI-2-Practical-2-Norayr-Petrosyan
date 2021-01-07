res = [int(elem) for elem in input("numbers:").split()]
max = res[0] * res[1]
for elem in range(len(res) - 1):
    curr = res[elem] * res[elem + 1]

    if curr > max:
        max = curr

print(max)