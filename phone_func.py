#from phone_func import show_all_contacts, find_contact, add_new_contact, change_contact, delete_contact

# s - показать контакты - complete
def show_all_contacts(file_name: str):
    pass
    # with open(file_name, 'r',encoding = 'utf-8') as file:
    #     for line in file:
    #         tmp = file.read(line)
    #         print(tmp.split(',')[1][2][3][4])
            #print(file.read())
        #print(file.readline())
        
# f - найти контакт
def find_contact(file_name: str):
    pass


# a - добавить запись

def count_lines(file: str):
    with open(file) as f:
        try:
            for i, _ in enumerate(f):
                pass
            return i + 1
        except:
            return 1

def add_contact(file: str):
    print('Для создания новой записи в телефонной книге введите пожалуйста фамилию, имя, отчество и номер телефона')
    l_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    p_name = input("Введите отчество: ")
    phone_num = input("Введите номер телефона: ")
    
    new_dict = {count_lines(file): [l_name, f_name, p_name, phone_num]}
    with open(file,'a',encoding='UTF-8') as f:
        f.write(f'{new_dict}\n')
        
# c - изменить контакт
def change_contact(file_name: str):
    pass

# d - удалить контакт
def delete_contact(file_name: str):
    pass
        

