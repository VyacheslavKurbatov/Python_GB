def reading_to_file(text: str) -> str:
    with open(f'{text}', 'r') as data:
        for file_for_decod in data:
            return file_for_decod


def cut_algorithm(some_text: str):
    new_list = []
    index = 0

    for i in range(1, len(some_text)):
        if some_text[i].isdigit():
            new_text = some_text[index:i]
            index = i
            new_list.append(new_text)

    new_text = some_text[index: len(some_text)-1]
    new_list.append(new_text)
    return new_list


def decode_algorithm(some_list: list):
    new_list = []
    for i in range(len(some_list)):
        decode_elem = ''
        item = some_list[i]
        elem = item[1]
        len_elem = int(item[0])
        for i in range(len_elem):
            decode_elem += elem
        new_list.append(decode_elem)

    new_string = ''
    for item in new_list:
        new_string += item
    return new_string


def writing_to_file(some_string: str):
    with open('decoded_file.txt', 'w') as data:
        data.writelines(f'{some_string}\n')


text_for_decoded = reading_to_file('compressed_file.txt')

list_for_decoded = cut_algorithm(text_for_decoded)

decoded_string = decode_algorithm(list_for_decoded)

writing_to_file(decoded_string)