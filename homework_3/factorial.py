number = int(input("Enter a number: "))

def factorial(number):
    factorial = 1
    for i in range(number):
        factorial *= i + 1
    return factorial

print(factorial(number))



