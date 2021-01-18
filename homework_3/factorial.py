number = int(input("Enter a number: "))

def factorial(value):
    factorial = 1
    for i in range(value):
        factorial *= i + 1
    return factorial

print(factorial(number))