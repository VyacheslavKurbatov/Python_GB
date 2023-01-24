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

    with open('NewDataBase.txt', 'w') as data:
        data.writelines(f'\n')
    for i, item in enumerate(new_db_list):
        with open('NewDataBase.txt', 'a') as data:
            data.writelines(f'{item}\n')
