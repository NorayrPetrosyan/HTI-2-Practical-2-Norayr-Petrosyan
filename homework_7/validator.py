import sys
import re

def validate_phone_number(number):
    pattern = '^0?(77|98|55|99|91)[\ -]?(\d{2}-\d{2}-\d{2}|\d{3}[\ -]?\d{3}|\d{2}[\ ]\d{2}[\ ]\d{2})$'
    if re.match(pattern,number):
        return True
    return False

def validate_email(email):
    pattern1 = '^[a-zA-Z0-9]+[_a-zA-Z0-9-.+]@[a-zA-Z0-9]+[a-zA-Z_.].+[A-Za-z]$'
    if re.match(pattern1, email):
        return True
    return False

if __name__ == '__main__':
    if len(sys.argv) > 2:
        command = sys.argv[1]
        value = sys.argv[2]

        if command == "phone_number":
            if validate_phone_number(value):
                print("Yes")
            else:
                print("No")

        elif command == "email":
            if validate_phone_number(value):
                print("Yes")
            else:
                print("No")

        else:
            print("No such command.")

    else:
        if len(sys.argv) == 2:
            if sys.argv[1] == "phone_number" or sys.argv[1] == "email":
                print("No value passed.")
            else:
                print("No such command.")

        else:
            print("Type one of the following commands.\nemail\nphone_number")