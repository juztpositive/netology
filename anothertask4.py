with open("web_clients_correct.csv") as file:
    info = file.readlines()

info.remove(info[0])
table_info = []

def get_age(age):
    ages_check = ["0", "5", "6", "7", "8", "9"]

    if len(age) >= 2 and age[-2:] in ["11", "12", "13", "14"]:
        return f"{age} лет"
    if age[-1] in ages_check:
        return f"{age} лет"
    elif age[-1] == "1":
        return f"{age} год"
    else:
        return f"{age} года"

def get_device(device):
    device_check = {
        "mobile": "мобильного",
        "tablet": "мобильного",
        "laptop": "компьютерного",
        "desktop": "компьютерного"
    }
    return device_check[device]

def is_female(gender):
    return gender == "female"

for line in info:
    info_split = line.split(",")
    isfemale = is_female(info_split[3])
    gender = "женского" if isfemale else "мужского"
    age_info = f'{get_age(info_split[4]) + (" совершила" if isfemale else " совершил")} покупку на'
    device_info = f'с {get_device(info_split[1])} браузера {info_split[2]}'
    region = f'Регион, из которого совершалась покупка: {info_split[6]}'
    username_info = f'Пользователь {info_split[0] + ' ' + gender} пола'

    string = f'{username_info}, {age_info} {info_split[5]} у.е. {device_info}. {region}'
    table_info.append(string)

with open("new2.txt", "w", encoding="utf-8") as info_newfile:
    info_newfile.writelines(table_info)
