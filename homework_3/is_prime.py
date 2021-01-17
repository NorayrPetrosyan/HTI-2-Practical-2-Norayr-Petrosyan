number = int(input("Enter a number: "))

def is_prime(number):
    if number > 1:
        p = 1
        for i in range(2, number // 2 + 1):
            p *= number % i
        if p == 0:
            return "No"
        else:
            return "Yes"
    else:
        return "No"

print(is_prime(number))


