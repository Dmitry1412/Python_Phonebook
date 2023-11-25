#from phone_func import show_all_contacts, find_contact, add_new_contact, change_contact, delete_contact

# s - показать контакты - complete
def show_contacts(file: str):
    print('*'*25)
    with open(file,encoding = 'utf-8') as f:
        for line in f:
            data = eval(line)
            num = list(data.keys())
            data = list(data.values())
            
            print(f'Фамилия: {data[0][0]}, Имя: {data[0][1]}, Отчество: {data[0][2]}, Телефон: {data[0][3]}')
    print('*'*25)
        
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
            return 0

def add_contact(file: str):
    print('Для создания новой записи в телефонной книге введите пожалуйста фамилию, имя, отчество и номер телефона')
    l_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    p_name = input("Введите отчество: ")
    phone_num = input("Введите номер телефона: ")
    
    new_dict = {count_lines(file): [l_name, f_name, p_name, phone_num]}
    with open(file,'a',encoding='UTF-8') as f:
        f.write(f'{new_dict}\n')
    print('*'*25)
    print("Контакт добавлен")
    print('*'*25)
        
# c - изменить контакт
def change_contact(file_name: str):
    pass

# d - удалить контакт
def delete_contact(file_name: str):
    pass
        

