passwords={
    "user" : "12345",
    "root" : "10 101",
    "admin" : "aaa"
}
passwords['marat']=['qwerty']
passwords.keys()
passwords.values()
print(passwords)
print(passwords.get("user"))

for name, password in passwords.items():
    print(name +password)
nick = input("Введите ваше имя: ")
pwd = input("Введите ваш пароль: ")
if nick in passwords:
    if passwords[nick] == pwd:
        print("Вы вошли в систему!")
    else:
        print("Неверный пароль!")
else:
    print("Такого пользователя нет!")