info = open("web_clients_correct.csv").readlines()
info.remove(info[0])
tableinformation = []

def checkage(age):
    agescheck = ['0', '5', '6', '7', '8', '9']

    if len(age) >= 2 and age[-2:] in ['11', '12', '13', '14']:
        return f'{age} лет'
    if age[-1] in agescheck:
        return f'{age} лет'
    elif age[-1] == '1':
        return f'{age} год'
    else:
        return f'{age} года'

def checkdevice(device):
    devicecheck = {
        'mobile': 'мобильного',
        'tablet': 'мобильного',
        'laptop': 'компьютерного',
        'desktop': 'компьютерного'
    }
    return devicecheck[device]

def checkgender(gender):
    return gender == 'female'

for line in info:
    splitedline = line.split(',')
    string = f'Пользователь {splitedline[0]} {checkgender(splitedline[3]) and "женского" or "мужского"} пола, {checkage(splitedline[4])} {checkgender(splitedline[3]) and "совершила" or "совершил"} покупку на {splitedline[5]} у.е. с {checkdevice(splitedline[1])} браузера {splitedline[2]}. Регион, из которого совершалась покупка: {splitedline[6].replace('\n','')}'
    tableinformation.append(string)
    tableinformation.append('\n')

newfile = open('test.txt', 'w', encoding='utf-8').writelines(tableinformation)
