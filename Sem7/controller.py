import model
import view


def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.read_db('database.txt')
            view.db_success(model.db_list)
        case 3:
            model.safe_contact()
            view.print_safe()
        case 4:
            model.create_contact(view.create_contact_contact_text[0],
                                 view.create_contact_contact_text[1],
                                 view.create_contact_contact_text[2],
                                 view.create_contact_contact_text[3],
                                 view.create_contact_contact_text[4])
        case 5:
            view.show_all(model.db_list)
            model.chage_contact(view.chage_contact_text[0],
                                view.chage_contact_text[1],
                                view.chage_contact_text[2],
                                view.chage_contact_text[3],
                                view.chage_contact_text[4],
                                view.chage_contact_text[5],)
        case 6:
            view.show_all(model.db_list)
            model.delete_contact(view.delete_contact_text[0],
                                 view.delete_contact_text[1])
        case 7:
            view.exit_program()

def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)