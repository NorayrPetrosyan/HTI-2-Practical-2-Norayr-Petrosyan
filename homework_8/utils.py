import sys

def odd_digits_checker(num):
    is_odd = True
    if num == 0:
        is_odd = False
    while num != 0:
        digit = num % 10
        if digit % 2 == 0:
            is_odd = False
            break
        num //= 10
    return is_odd

def has_only_odd_digits(start, stop):
    for number in range(start, stop):
        if odd_digits_checker(number):
            yield number

if __name__ == "__main__":
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
    for odd_number in has_only_odd_digits(start,stop):
        print(odd_number, end=' ')