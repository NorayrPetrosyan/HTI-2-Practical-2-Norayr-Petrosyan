number = int(input("Enter a number: "))
def number_root(number):
    p = 0
    for i in range(len(str(number))):
        p = p + ((number // 10**i) % 10)
    number = p
    while len(str(number)) != 1:
        number = number_root(number)
    if len(str(number)) == 1:
        return number
print(number_root(number))







