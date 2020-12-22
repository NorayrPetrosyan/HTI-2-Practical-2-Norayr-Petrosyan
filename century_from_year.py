year = int(input('Enter a year: '))

if year % 100 == 0:
    print('The century: ', year // 100)
else:
    print('The century: ', year // 100 + 1)