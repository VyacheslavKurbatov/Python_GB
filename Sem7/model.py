db_list = []


def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)
    return db_list


def safe_contact():
    global db_list
    new_db_list = []
    for i, item in enumerate(db_list):
        new_db_list.append(list(item.values()))
    for i, item in enumerate(new_db_list):
        new_db_list[i] = f'{item[0]};{item[1]};{item[2]};{item[3]}'

    with open('database.txt', 'w') as data:
        data.writelines('')
    for i, item in enumerate(new_db_list):
        with open('database.txt', 'a') as data:
            data.writelines(f'{item}\n')


def create_contact(text_0, text_1, text_2, text_3, text_4):
    print(text_0)
    new_contact = dict()

    new_contact['lastname'] = input(f'\t{text_1}')
    new_contact['firstname'] = input(f'\t{text_2}')
    new_contact['phone'] = input(f'\t{text_3}')
    new_contact['comment'] = input(f'\t{text_4}')
    db_list.append(new_contact)


def chage_contact(text_0, text_1, text_2, text_3, text_4, text_5):
    global db_list

    while True:
        try:
            num_contact = int(input(text_0))
            break
        except:
            print(text_1)

    new_contact = dict()

    new_contact['lastname'] = input(f'\t{text_2}')
    new_contact['firstname'] = input(f'\t{text_3}')
    new_contact['phone'] = input(f'\t{text_4}')
    new_contact['comment'] = input(f'\t{text_5}')
    db_list[num_contact - 1] = new_contact


def delete_contact(text_0, text_1):
    global db_list

    while True:
        try:
            num_contact = int(input(text_0))
            break
        except:
            print(text_1)

    db_list.pop(num_contact-1)