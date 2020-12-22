year = int(input('Enter a year: '))

if year % 100 == 0:
    print(year // 100)
else:
    print(year // 100 + 1)