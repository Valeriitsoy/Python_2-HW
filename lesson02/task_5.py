# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5)


number = int(input('Введите натуральное число: '))
even_digit = 0
odd_digit = 0

while number > 0:
    number = number // 10
    if number % 2 == 0:
        even_digit += 1
    else:
        odd_digit += 1

print(f'Четных цифр - {even_digit}, нечетных цифр - {odd_digit}')
