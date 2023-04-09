def file_read():
    with open('phonebook.txt', 'r', encoding='utf-8') as fin:
        data = []
        for line in fin:
            data.append(line.strip('\n').split())
    return data

def display_all_records():
    data = file_read()
    for row in data:
        print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_last_name():
    last_name = input('Введите фамилию: ')
    data = file_read()
    for row in data:
        if row[0] == last_name:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_phone_number():
    phone = input('Введите номер телефона: ')
    data = file_read()
    for row in data:
        if row[2] == phone:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def data_app():
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        info = input('Введите данные абонента (фамилия, имя, номер, комментарий - через пробел): ').split(' ')
        file.write(' '.join(info))
        print('Данные записаны.')


def delet_data():
    delet_1 = input('Введите фамилию человека, которого хотите удалить: ')
    data = []
    list = []
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip('\n').split())
    for elem in data:
        if elem[0] == delet_1:
            data.remove(elem)
    for i in data:
        if i == data[0]:
            files = open('phonebook.txt', 'w', encoding='utf-8')
            files.writelines(' '.join(map(str, i)) + '\n')
        else:
            files = open('phonebook.txt', 'a', encoding='utf-8')
            files.writelines(' '.join(map(str, i)) + '\n')


number = 0
while number != '6':
    print('Введите число для операции со справочником:')
    print('1 - вывести весь справочник;\n2 - найти абонента по фамилии;\n'
          '3 - найти абонента по номеру телефона;\n4 - ввести данные нового абонента;\n5 - удаление данных;\n6 - завершить работу.')

    number = input()

    if number == '1':
        display_all_records()

    elif number == '2':
        find_last_name()

    elif number == '3':
        find_phone_number()

    elif number == '4':
        data_app()
    
    elif number == '5':
        delet_data()

else:
    print('Работа завершена.')
