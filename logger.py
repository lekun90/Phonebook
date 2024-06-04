from data_create import name_data, surname_data, address_data, phone_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant', 'a', encoding='utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {address}\n")

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        print(data_first)
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
    print(*data_first_list)

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
    print(*data_second)

def read_file_to_list_2():
    with open('data_second_variant', 'r', encoding='utf-8') as f:
        data_second_list = []
        for line in f.readlines():
            data_second_list.append(line.split('; '))
    return data_second_list

def read_file_to_list_1():
    with open('data_first_variant', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        print(data_first)
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                line = ''.join(data_first[j:i])
                data_first_list.append(line.split('\n'))
                j = i+1
    return data_first_list

def search_parameters():
    print("По какому полю выполнить поиск? \n 1 - по имени \n 2 - по фамилии \n 3 - по номеру телефона")
    search_field = int(input('Введите число '))

    while search_field != 1 and search_field != 2 and search_field != 3:
        print("Неправильный ввод")
        search_field = int(input('Введите число '))

    search_value = None
    if search_field == 1:
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == 2:
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == 3:
        search_value = input('Введите номер для поиска: ')
        print()
    return str(search_field), search_value

def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {"; ".join(search_result[i])}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        return search_result
    print()

def change_data():
    contact_list = read_file_to_list_2()

    number_to_change = search_to_modify(contact_list)
    if len(number_to_change) != 0:
        contact_list.remove(number_to_change)
        print('Какое поле вы хотите изменить?')
        field = input('1 - Имя\n2 - Фамилия\n3 - Номер телефона\n4 - Адресс\nВведите число: ')
        if field == '1':
            number_to_change[0] = input('Введите имя: ')
        elif field == '2':
            number_to_change[1] = input('Введите фамилию: ')
        elif field == '3':
            number_to_change[2] = input('Введите номер телефона: ')
        elif field == '4':
            number_to_change[3] = input('Введите адресс: ')
        contact_list.append(number_to_change)

        with open('data_second_variant', 'w', encoding='utf-8') as f:
            for contact in contact_list:
                #line = '; '.join(contact) + '\n'
                line = '; '.join(contact)
                f.write(line)

        with open('data_first_variant', 'w', encoding='utf-8') as f:
            for contact in contact_list:
                line = '\n'.join(contact) + '\n\n'
                f.write(line)

        print('Изменения внесены!')
    else:
        print('Контакт не найден')

def delete_data():
    contact_list = read_file_to_list_2()
    number_to_change = search_to_modify(contact_list)
    if len(number_to_change) != 0:
        contact_list.remove(number_to_change)

        with open('data_second_variant', 'w', encoding='utf-8') as f:
            for contact in contact_list:
                line = '; '.join(contact)
                f.write(line)

        with open('data_first_variant', 'w', encoding='utf-8') as f:
            for contact in contact_list:
                line = '\n'.join(contact) + '\n\n'
                f.write(line)

        print('Контакт удален!')
    else:
        print('Контакт не найден')

change_data()
