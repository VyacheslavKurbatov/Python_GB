def reading_to_file(text: str) -> str:
    with open(f'{text}', 'r') as data:
        for some_list in data:
            return some_list

list_for_rle = reading_to_file('file_for_read.txt')
print(list_for_rle)