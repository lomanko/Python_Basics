# Задача 1

side_sqr = int(input('Введите длину стороны квадрата:'))
perimeter_sqr = side_sqr * 4
area_sqr = side_sqr ** 2
print('\nПериметр:', perimeter_sqr)
print('Площадь:', area_sqr)

side_1_rectangle = int(input('\nВведите длину прямоугольника:'))
side_2_rectangle = int(input('Введите ширину прямоугольника:'))
perimeter_rectangle = (side_1_rectangle + side_2_rectangle) * 2
area_rectangle = side_1_rectangle * side_2_rectangle
print('\nПериметр:', perimeter_rectangle)
print('Площадь:', area_rectangle)

# Задача 3

separate_symbol = input('\nВведите символ для разделителя задач:')
repeat = perimeter_sqr + area_rectangle
print(separate_symbol * repeat)


# Задача 2

salary = float(input('\nВведите заработную плату в месяц:'))
mortgage_rate = float(input('Введите, какой процент(%) уходит на ипотеку:'))
life_rate = float(input('Введите, какой процент(%) уходит на жизнь:'))

mortgage_spent = salary * (mortgage_rate / 100) * 12
life_spent = salary * (life_rate / 100) * 12
money_stock = salary * 12 - mortgage_spent - life_spent

print(f'\nНа ипотеку было потрачено:{mortgage_spent} рублей')
print(f'Было накоплено:{money_stock} рублей')
