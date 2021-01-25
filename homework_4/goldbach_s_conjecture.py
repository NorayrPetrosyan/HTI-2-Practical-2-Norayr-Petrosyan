def is_prime(the_number):
    is_primee = True

    if the_number <= 1:
        is_primee = False

    for i in range(2, the_number // 2 + 1):
        if the_number % i == 0:
            is_primee = False
            break

    return is_primee


def goldbach_s_conjecture(number):
    if number <= 2:
        return "Wrong input"

    for big_amount in range(number, 0, -1):
        if is_prime(big_amount):
            small_amount = number - big_amount

            if is_prime(small_amount):
                break

    return f'{small_amount} {big_amount}'

my_number = int(input("Enter a postive number bigger than 2: "))
print(goldbach_s_conjecture(my_number))