import sys


number = int(input('Введите натуральное число: '))
sum_memory = 0
sum_memory += sys.getsizeof(number)
print(sys.getsizeof(number))

even_digit = 0
odd_digit = 0

while number > 0:
    if number % 2 == 0:
        even_digit += 1
    else:
        odd_digit += 1
    number = number // 10

sum_memory += sys.getsizeof(even_digit)
print(sys.getsizeof(even_digit))
sum_memory += sys.getsizeof(odd_digit)
print(sys.getsizeof(odd_digit))

print(f'Четных цифр - {even_digit}, нечетных цифр - {odd_digit}')
print(f'Памяти занято {sum_memory}')

# Вводим 1234 память 42