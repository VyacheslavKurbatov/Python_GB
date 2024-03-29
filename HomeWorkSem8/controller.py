import model
import view


def input_command_second_menu(inp: int, text: str):
    match inp:
        case 1:
            start_lesson(text)
        case 2:
            while True:
                student_stat_name = view.who_answer()
                if student_stat_name == 'exit':
                    break
                elif model.check_student(student_stat_name):
                    view.statistics(model.class_dict, student_stat_name)
                else:
                    print(view.mistake[3])
                    print(view.mistake[1])
                    print(view.mistake[0])
        case 3:
            start()

def start():

    while True:
        input_class = view.input_class()
        if input_class == 'exit':
            exit()
        else:
            try:
                model.read_class(input_class)
                while True:
                    input_command_second_menu(view.second_menu(), input_class)
            except:
                print(view.mistake[2])
                print(view.mistake[1])
                print(view.mistake[0])



def start_lesson(class_num: str):
    check_less = False
    while check_less == False:
        user_inp_lesson = view.lesson_menu()
        check_less = model.check_lesson(user_inp_lesson)
        if check_less == False:
            print(view.mistake[4])

    lesson_student_dict = model.lesson(user_inp_lesson)
    view.all_student(lesson_student_dict)

    student = ''
    while True:
        student = view.who_answer()
        if student == 'exit':
            model.save_file(class_num)
            break
        elif model.check_student(student):

            mark = int(view.what_mark())
            model.student_mark(student, mark)
            view.all_student(lesson_student_dict)
        else:
            print(view.mistake[3])
            print(view.mistake[1])
            print(view.mistake[0])