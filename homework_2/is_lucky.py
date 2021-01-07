res = int(input("number:"))
res1 = [int(elem1) for elem1 in str(res)]
sum1 = 0
sum2 = 0
if (len(res1)) % 2 == 0:
    for elem in range(len(res1) // 2):
        sum1 = sum1 + [elem]
        sum2 = sum2 + res1[len(res1)-elem-1]
    if sum1 == sum2:
        print("Yes")
    else:
        print("No")