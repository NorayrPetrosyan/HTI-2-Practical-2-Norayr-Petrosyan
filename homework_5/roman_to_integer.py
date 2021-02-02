def roman_to_integer(num):
    sum = 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(len(num) - 1):
        if values[num[i]] < values[num[i+1]]:
            sum -= ((values[num[i]] + values[num[i+1]]) - (values[num[i+1]] - values[num[i]]))

    for j in range(len(num)):
        sum += values[num[j]]

    return sum


print(roman_to_integer(input("Enter a number: ")))