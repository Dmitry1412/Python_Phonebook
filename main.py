from phone_func import show_contacts, find_contact, add_contact, count_lines, change_contact, delete_contact 

def main():
    file_name = 'phone_book.txt'
    flag_exit = False
    while not flag_exit:
        print('s - показать контакты')
        print('f - найти контакт')
        print('a - добавить контакт')
        print('c - изменить контакт')
        print('d - удалить контакт')
        answer = input('Введите операцию или Х для выхода: ')
        if answer == 's':
            show_contacts(file_name)
        elif answer == 'f':
            find_contact(file_name)
        elif answer == "a":
            add_contact(file_name)
        elif answer == 'c':
            change_contact(file_name)
        elif answer == 'd':
            delete_contact(file_name)
        elif answer == "x":
            flag_exit = True
            
main()
