# Задание 1

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
  boys.sort()
  girls.sort()
  print('Идеальные пары:')
  for boy, girl in zip(boys,girls):
    print(f'{boy} и {girl}')
else:
  print('Внимание! Кто-то может остаться без пары!')

# Задание 2

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]  
]

person = 5

print()

for dish_name, ingridient in cook_book:
  print(f'{dish_name.capitalize()}:')
  for ingridient_name, quantity, dimension in ingridient:
    print(f'{ingridient_name}: {quantity * person}{dimension}')
  print()


