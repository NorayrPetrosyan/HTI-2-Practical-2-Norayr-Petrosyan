number = int(input("Enter a number: "))

def number_root(value):
    result = 0
    for i in range(len(str(value))):
        result = result + ((value // 10**i) % 10)
    value = result
    while len(str(value)) != 1:
        value = number_root(value)
    if len(str(value)) == 1:
        return value

print(number_root(number))