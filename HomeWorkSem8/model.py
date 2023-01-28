class_dict = {}
lesson_student_dict = {}

def read_class(path: str):
    global class_dict
    path = path + '.txt'
    with open(path, 'r', encoding='UTF-8') as file:
        class_list = file.readlines()

    student_list = []
    for i, item in enumerate(class_list):
        item = item.rstrip().split('|')

        student_list = item[1].split('&')
        student_dict = {}

        for student in student_list:
            value = student.split(':')
            value[1] = value[1].split()
            value[1] = list(map(int, value[1]))
            student_dict[value[0]] = value[1]

        class_dict[item[0]] = student_dict



def lesson(text: str):
    global class_dict
    global lesson_student_dict

    for key, value in class_dict.items():
        if text in key:
            lesson_student_dict = value
            return lesson_student_dict

def student_mark(student: str, mark: int):
    global lesson_student_dict
    marks = lesson_student_dict.get(student)
    marks.append(mark)
    lesson_student_dict[student] = marks


def save_file(path: str):
    global class_dict
    path = path + '.txt'
    subject = ''
    all_list = []
    for key, value in class_dict.items():
        subject = key
        student_list = value
        st_list = []

        for student, mark_list in student_list.items():
            st_list.append(student + ':' + ' '.join(list(map(str, mark_list))))
        all_list.append(subject + '|' + '&'.join(st_list))


    with open(path, 'w', encoding='UTF-8') as data:
        data.writelines('')
    for i, item in enumerate(all_list):
        with open(path, 'a', encoding='UTF-8') as data:
            data.writelines(f'{item}\n')


def check_student(inp_stud):
    global class_dict

    for key, value in class_dict.items():
        student_dict = value
        student_list = []

        for student, mark_list in student_dict.items():
            student_list.append(student)

        if inp_stud in student_list:
            return True
        else:
            return False


def check_lesson(inp_lesson):
    global class_dict
    lesson_list = []
    for key, value in class_dict.items():
        lesson_list.append(key)

    if inp_lesson in lesson_list:
        return True
    else:
        return False