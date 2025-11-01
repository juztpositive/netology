from datetime import datetime
newspapers = {
    'The Moscow Times': {'Date': 'Wednesday, October 2, 2002', 'Format': "%A, %B %d, %Y"},
    'The Guardian': {'Date': 'Friday, 11.10.13', 'Format': "%A, %d.%m.%y"},
    'Daily News': {'Date': 'Thursday, 18 August 1977', 'Format': "%A, %d %B %Y"},
}

while True:
    command = input('Введите команду:\n')
    if command != 'q':
        try:
            print(command + f' — {datetime.strptime(newspapers[command]['Date'], newspapers[command]['Format'])}')
        except KeyError:
            print('Неверная команда, попробуйте ввести правильное название газеты')
    else:
        break
