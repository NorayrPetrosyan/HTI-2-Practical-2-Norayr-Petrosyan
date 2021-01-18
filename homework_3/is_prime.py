number = int(input("Enter a number: "))

def is_prime(value):
    if value > 1:
        result = 1
        for i in range(2, value // 2 + 1):
            result *= value % i
        if result == 0:
            return False
        else:
            return True
    else:
        return False

if is_prime(number):
    print('Yes')
else:
    print('No')

# THE SECOND OPTION
#
# number = int(input("Enter a number: "))
#
# def is_prime(value):
#     if value > 1:
#         result = 1
#         for i in range(2, value // 2 + 1):
#             result *= value % i
#         if result == 0:
#             return "No"
#         else:
#             return "Yes"
#     else:
#         return "No"
#
# print(is_prime(number))