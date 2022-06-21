from pprint import pprint
import os

def recipes_dict(recipe_file):
    '''
    Функция для преобразования файла рецептов в словарь.
    '''
    cook_book = {}
    with open(recipe_file) as recipe_file:
        for line in recipe_file:
            name_dish = line.strip() #строка с названием блюда
            number_ingredients = int(recipe_file.readline()) #строка с количеством ингредиентов
            ingredient_list =[] #список для ингредиентов
            for item in range(number_ingredients): #цикл по количеству ингредиентов
                line = recipe_file.readline().strip().split('|') #разбиваем строку на список из 3-х элементов: название ингредиента, размерность, количество
                ingredient_list.append({'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]}) #добавляем в список ингредиент в форме словаря
            cook_book[name_dish] = ingredient_list #создаем элемент итогового словаря
            recipe_file.readline()
    return cook_book

print('Задача 1.')
print('Полученный словарь рецептов:\n')
pprint(recipes_dict('recipes.txt'),width=100,sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    '''
    Функция принимает на вход список блюд и количество персон.
    В результате словарь из необходимых ингредиентов.
    '''
    dict_of_ingridients = {}
    for dish in dishes: #для каждого блюда в dishes
        for ingredient in recipes_dict('recipes.txt')[dish]: #для каждого ингридиента в блюде (используется функция recipes_dict)
            if dict_of_ingridients.get(ingredient['ingredient_name']) == None: #проверка есть ингридиент или нет
                #если нет, то добавляем в словарь
                dict_of_ingridients[ingredient['ingredient_name']] = {'measure': ingredient['measure'],'quantity': int(ingredient['quantity']) * person_count}
            else:
                #если есть, то обновляем значение словаря для ингридиента
                dict_of_ingridients[ingredient['ingredient_name']]['quantity'] += (int(ingredient['quantity']) * person_count)
    return dict_of_ingridients

print('\nЗадача 2.')
print('Полученный словарь ингридиентов:\n')
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель','Омлет'],1),width=100,sort_dicts=False)

def sorted_file_print (folder_name):
    '''
    Функция берёт выбранную папку из текущей директории
    и создаёт новый файл с содержимым файлов из папки отсортированных по количеству строк.

    '''
    folder_path = os.path.join(os.getcwd(), folder_name) #путь к папке с файлами в текущей директории
    file_list = sorted(os.listdir(folder_path)) #список файлов в директории
    
    file_size ={}
    for file in file_list: #создание словаря с количеством строк в файлах
        file_path = os.path.join(folder_path, file)
        with open(file_path) as f:
            file_size[file] = sum(1 for line in f)
    
    files_sorted = sorted(file_size, key=file_size.get) #сортировка названий файлов по количеству строк
    
    open('concatenate_file.txt', 'w').close() #очистка итогового файла перед записью
    for file in files_sorted:
        file_path = os.path.join(folder_path, file)
        with open('concatenate_file.txt','a') as f: #в новый файл пишем последовательно для каждого файла
            f.write(f'{file}\n') #название файла
            f.write(f'{file_size[file]}\n') #количество строк в файле
            with open(file_path) as file_for_append: #содержимое файла
                f.write(f'{file_for_append.read()}\n') 
    return

sorted_file_print ('sorted')