def reading_to_file(text: str) -> str:
    with open(f'{text}', 'r') as data:
        for file_for_RLE in data:
            return file_for_RLE

def cut_algorithm(some_text: str):
    new_list = []
    index = 0

    for i in range(1, len(some_text)):
        if some_text[i] != some_text[i - 1]:
            new_text = some_text[index:i]
            index = i
            new_list.append(new_text)

    new_text = some_text[index:len(some_text)]
    new_list.append(new_text)
    return new_list

def change_algorithm(some_list: list):
    new_list = []
    for i in range(len(some_list)):
        elem = some_list[i]
        str_count = str(len(some_list[i]))
        res = str_count + elem[0]
        new_list.append(res)

    new_string = ''
    for item in new_list:
        new_string += item
    return new_string

def writing_to_file(some_string: str):
    with open('compressed_file.txt', 'w') as data:
        data.writelines(f'{some_string}\n')


text_for_RLE = reading_to_file('file_for_read.txt')

cuted_list = cut_algorithm(text_for_RLE)

compressed_text = change_algorithm(cuted_list)
writing_to_file(compressed_text)