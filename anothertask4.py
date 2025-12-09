info = open("web_clients_correct.csv").readlines()
info.remove(info[0])
tableinformation = []

def checkage(age):
    agescheck = ["0", "5", "6", "7", "8", "9"]

    if len(age) >= 2 and age[-2:] in ["11", "12", "13", "14"]:
        return f"{age} лет"
    if age[-1] in agescheck:
        return f"{age} лет"
    elif age[-1] == "1":
        return f"{age} год"
    else:
        return f"{age} года"

def checkdevice(device):
    devicecheck = {
        "mobile": "мобильного",
        "tablet": "мобильного",
        "laptop": "компьютерного",
        "desktop": "компьютерного"
    }
    return devicecheck[device]

def checkgender(gender):
    return gender == "female"

for line in info:
    splitedline = line.split(",")
    username = splitedline[0]
    gender = "женского" if checkgender(splitedline[3]) else "мужского"
    gendersecond = "совершила" if checkgender(splitedline[3]) else "совершил"
    age = checkage(splitedline[4])
    device = checkdevice(splitedline[1])
    browser = splitedline[2]
    region = splitedline[6]

    string = f'Пользователь {username} {gender} пола, {age} {gendersecond} покупку на {splitedline[5]} у.е. с {device} браузера {browser}. Регион, из которого совершалась покупка: {region}'
    tableinformation.append(string)

newfile = open("new.txt", "w", encoding="utf-8").writelines(tableinformation)
