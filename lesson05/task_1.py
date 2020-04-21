from collections import defaultdict

quantity = int(input("Введите количество предприятий:  "))
quarter = 4
list_ = []
for i in range(quantity):
    name = input(f'Введите название {i + 1}: ')
    for a in range(quarter):
        profit = int(input(f'Введите прибыль за {a + 1} квартал: '))
        t = name, profit
        list_.append(t)

dict_ = defaultdict(list)
for key, value in list_:
    dict_[key].append(value)

j = dict_.items()
result = {}
for name, profit in j:
    s_ = sum(profit)
    keys = name
    val = s_
    result[keys] = val

m = dict_.values()
sum_values = list(m)
d = []
for e in sum_values:
    d += e
sum_ = sum(d)
average = sum_ / quantity
print(f'Средняя прибыль {quantity}-х предприятий за год = {round(average, 2)}')

for name, profit in result.items():
    if profit > average:
        print(f'{name} прибыль выше среднего - {profit}')
    elif profit < average:
        print(f'{name} прибыль ниже среднего - {profit}')
