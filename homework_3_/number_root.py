number = int(input("Enter a number: "))

def number_root(number):
    result = 0
    for i in range(len(str(number))):
        result = result + ((number // 10**i) % 10)
    number = result
    while len(str(number)) != 1:
        number = number_root(number)
    if len(str(number)) == 1:
        return number

print(number_root(number))