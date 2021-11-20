odd_numbers = []
for i in range(1, 1000):
    if i % 2 != 0:
        odd_numbers.append(i**3)
i = 0
amount_digits_7 = 0
for element in odd_numbers:
    amount_digits = 0
    while element > 0:
        digit = element % 10
        amount_digits = amount_digits + digit
        element = element // 10
    if amount_digits % 7 == 0:
        amount_digits_7 += odd_numbers[i]
    i += 1
print('Cписок, из кубов нечётных чисел: ', odd_numbers)
print('Сумма чисел: ', amount_digits_7)
i = 0
for element in odd_numbers:
    odd_numbers[i] = element + 17
    i += 1
print('Cписок, из кубов нечётных чисел +17: ', odd_numbers)
i = 0
amount_digits_17 = 0
for element in odd_numbers:
    amount_digits = 0
    while element > 0:
        digit = element % 10
        amount_digits = amount_digits + digit
        element = element // 10
    if amount_digits % 7 == 0:
        amount_digits_17 += odd_numbers[i]
    i += 1
print('Сумма чисел: ', amount_digits_17)