documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def help_list():
    '''
    Выводит список доступных комманд
    '''
    print('Список доступных комманд:')
    print('p - people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит.')
    print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится.')
    print('l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"')
    print('a - add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')
    print('d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.')
    print('m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.')
    print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.')
    return

def check_doc_id(doc_id,docs_list):
    '''
    Проверка наличия документа в базе.
    '''
    check = False
    for document in docs_list:
        if document['number'] == doc_id: check = True
    return check


def people(docs_list):
    '''
    Команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    '''
    doc_id = input('Введите номер документа для поиска владельца: ')
    if check_doc_id(doc_id,docs_list):
        for document in docs_list:
            if document['number'] == doc_id:
                print(f'Владелец документа нормер {doc_id}: {document["name"]}.')
    else:
        print(f'Документа с нормером {doc_id} нет в базе.')
    return
    

def shelf(docs_list, dir_dict):
    '''
    Команда, которая спросит номер документа и выведет номер полки, на которой он находится.
    '''
    doc_id = input('Введите номер документа для поиска полки: ')
    if check_doc_id(doc_id,docs_list):
        for key, value in dir_dict.items():
            if doc_id in value:
                print(f'Документ номер {doc_id} находится на полке с номером {key}')
    else:
        print(f'Документа с нормером {doc_id} нет в базе.')
    return

def show_list(docs_list):
    '''
    Команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    '''
    print('\nСписок всех документов в базе:\n')
    for document in docs_list:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')
    print()
    return

def add_document(docs_list,dir_dict):
    '''
    Команда, которая добавит новый документ в каталог и в перечень полок.
    Команда спросит его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    '''
    doc_id = input('Введите номер документа для добавления: ')
    while check_doc_id(doc_id,docs_list):
        print(f'Документ с номером {doc_id} уже существует, попробуйте другой номер.')
        doc_id = input('Введите номер документа для добавления: ')
    doc_type = input('Введите тип документа: ')
    doc_name = input('Введите имя владельца: ')
    doc_shelf = input('Введите номер полки для документа: ')
    while doc_shelf not in dir_dict.keys():
        print('Вы пытаетесь добавить документ на несуществующую полку, попробуйте другой номер полки.')
        doc_shelf = input('Введите номер полки для документа: ')
    
    docs_list.append({"type": doc_type, "number": doc_id, "name": doc_name})
    dir_dict[doc_shelf].append(doc_id)

    return

def del_document(docs_list,dir_dict):
    '''
    Команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
    '''
    doc_id = input('Введите номер документа для удаления: ')
    if not check_doc_id(doc_id,docs_list):
        print(f'Документа с номером {doc_id} нет в базе.')
    else:
        for document in docs_list:
            if document['number'] == doc_id:
                docs_list.remove(document)
                break
        for key, value in dir_dict.items():
            if doc_id in value:
                dir_dict[key].remove(doc_id)
        print(f'Документ номер {doc_id} успешно удалён из базы.')
    return

def move_document(docs_list, dir_dict):
    '''
    Команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    '''
    doc_id = input('Введите номер документа для перемещения: ')
    if not check_doc_id(doc_id,docs_list):
        print(f'Документ {doc_id} нельзя переместить, т.к. его не существует.')
    else:
        doc_shelf = input('Введите номер полки для перемещения: ')
        while doc_shelf not in dir_dict.keys():
            print('Вы пытаетесь переместить документ на несуществующую полку, попробуйте другой номер полки.')
            doc_shelf = input('Введите номер полки для перемещения: ')
        for key,value in dir_dict.items():
            if doc_id in value:
                dir_dict[key].remove(doc_id)
        dir_dict[doc_shelf].append(doc_id)
        print(f'Документ {doc_id} перемещен на полку номер {doc_shelf}.')

    return

def new_shelf(dir_dict):
    '''
    Команда, которая спросит номер новой полки и добавит ее в перечень.
    '''
    new_shelf = input('Введите номер новой полки для добавления: ')
    if new_shelf in dir_dict.keys():
        print(f'Нельзя добавить полку с номером {new_shelf}, т.к. она уже существует.')
        print(f'Список существующих полок: {list(dir_dict.keys())}.')
    else:
        dir_dict[new_shelf] = []
        print(f'Новая полка с номером {new_shelf} добавлена успешно.')
        print(f'Список существующих полок: {list(dir_dict.keys())}.')

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'h':
            help_list()
        elif command == 'p':
            people(documents)
        elif command == 's':
            shelf(documents,directories)  
        elif command == 'l':
            show_list(documents) 
        elif command == 'a':
            add_document(documents,directories)
        elif command == 'd':
            del_document(documents,directories)
        elif command == 'm':
            move_document(documents,directories)
        elif command == 'as':
            new_shelf(directories)
        elif command == 'q':
            return 
        else:
            print('Такой команды не существует. Для вызова списка команд введите h')

main()