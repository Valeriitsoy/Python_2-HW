# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

number = int(input("Введите натуральное число:  "))
max_s = 0
max_n = 0
while number != 0:
    max_num = number
    sum_digit = 0
    while number > 0:
        sum_digit += number % 10
        if sum_digit > max_s:
            max_s = sum_digit
            max_n = max_num
        number //= 10
    number = int(input("Введите натуральное число:  "))
print(f'Число {max_n}, имеет максимальную сумму цифр: {max_s}')
