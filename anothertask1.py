documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

while True:
    command = input('Введите команду:\n')
    if command == 'p':
        docnum = input('Введите номер документа:\n')
        for i in documents:
            if i['number'] == docnum:
                print(f'Результат:\nВладелец документа: {i['name']}')
    elif command == 's':
        docnum = input('Введите номер документа:\n')
        for k, v in directories.items():
            if v.__contains__(docnum):
                print(f'Результат:\nДокумент хранится на полке: {k}')
    elif command == 'q':
        break
