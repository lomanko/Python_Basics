# Задание 1
print('Задание 1\n')

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# Перебираем словари и ищем в значениях словаря Россию.
# Если она там есть, оставляем.
geo_logs = [visit for visit in geo_logs if 'Россия' in list(visit.values())[0]]

from pprint import pprint # импортируем, чтобы вывести словарь на печать красиво
pprint(geo_logs)

# Задание 2
print('\nЗадание 2\n')

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

geo_id =[]
# Создаем список из всех гео-ID (перебираем каждое значение внутри каждого списка)
geo_id = [item for users in ids.values() for item in users]
geo_id = set(geo_id) # Оставляем только уникальные значение
geo_id = list(geo_id) # Преобразуем обратно в список
print(f'Уникальные значения гео-ID: {geo_id}')

# Задание 3
print('\nЗадание 3\n')

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

# Посчитаем длины всех запросов в списке
len_queries = [len(query.split()) for query in queries]

# Для каждой уникальной длины посчитаем, сколько запросов с такой длиной.
for quantity in set(len_queries):
  print(f'Запросов, содержащих {quantity} слов(а): {len_queries.count(quantity) / len(queries) :.2%}')

# Задание 4
print('\nЗадание 4\n')

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

maximum = 0
name = None

# Цикл по всем ключам и значениям в поисках максимального.
for key, value in stats.items():
  if value > maximum:
    maximum = value
    name = key

print(name)

# Более быстрый способ через max и параметр key.
print(max(stats,key=stats.get))

# Задание 5
print('\nЗадание 5\n')

list_ = ['2018-01-01', 'yandex', 'cpc', 100]
dict = {list_[-1] : list_[-2]} # Первый шаг

# Цикл в обратном порядке для оставшихся значений списка.
for items in range(-3,-len(list_)-1,-1):
  dict = {list_[items] : dict}

print(dict)
