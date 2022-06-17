class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def get_info(self, x):
        return f'{self.name} {self.surname}, г. {self.city}, {x}'
    def __str__(self):
        return f'«{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.»'
cl1 = Client('Иван', 'Петров', 'Москва', 50)
cl2 = Client('Вася', 'Пупкин', 'Уфа', 200)
clients = [cl1, cl2]
for client in clients:
    print(client.get_info(10))