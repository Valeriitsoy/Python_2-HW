import sys


number = int(input('Введите натуральное число: '))
sum_memory = 0
sum_memory += sys.getsizeof(number)
print(sys.getsizeof(number))

dict_ = {}
value1 = 0
value2 = 0
while number > 0:
    if number % 2 == 0:
        value1 += 1
        dict_['even_digit'] = value1
    else:
        value2 += 1
        dict_['odd_digit'] = value2
    number = number // 10

sum_memory += sys.getsizeof(dict_)
print(sys.getsizeof(dict_))
sum_memory += sys.getsizeof(value1)
print(sys.getsizeof(value1))
sum_memory += sys.getsizeof(value2)
print(sys.getsizeof(value2))

print(dict_)
print(f'Памяти занято {sum_memory}')

#Вводим 1234 память 170