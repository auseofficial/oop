#TASK_1_Encapsulation##

# class Bank:
#     def __init__(self, account_number, account_holder, initial_balance=0):
#         self.acc_num = account_number
#         self.acc_hol = account_holder
#         self.balance = initial_balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. Total balance: {self.get_balance()}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. Total balance: {self.get_balance()}")

#     def get_balance(self):
#         return self.balance

# acc1 = Bank(123456, "Akib Us Suny Eshan", 0)
# acc1.deposit(10)
# acc1.withdraw(500)

# class Bank:
#     def __init__(self, account_number, account_holder, initial_balance=0):
#         self.acc_num = account_number
#         self.acc_hol = account_holder
#         self.balance = initial_balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. Total balance: {self.get_balance()}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. Total balance: {self.get_balance()}")

#     def get_balance(self):
#         return self.balance

#     def __str__(self):
#         return (f"Account Number: {self.acc_num}, Account Holder: {self.acc_hol}, Balance: {self.balance}")

# acc1 = Bank(123456, "Akib Us Suny Eshan", 0)
# acc1.deposit(1000)
# acc1.withdraw(500)
# print(acc1)  

# title = "1984"
# author = "George Orwell"
# year = 1949

# info = (f"Title: {title}, Author: {author}, Year: {year}")
# print(info)


# ##TASK_2_##
# class Item:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def get_info(self):
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

#     def __str__(self):
#         return self.get_info()


# class Person:
#     def __init__(self, name, age, height, weight): 
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight


# class Cricketer(Person):
#     def __init__(self, name, age, height, weight): 
#         super().__init__(name, age, height, weight)

#     def __lt__(self, other):
#         return self.age < other.age


# Sakib = Cricketer('Sakib', 38, 68, 91)
# Mushfiq = Cricketer('Mushfiq', 36, 55, 82)
# Mustafiz = Cricketer('Mustafiz', 27, 69, 86)
# Riyad = Cricketer('Riyad', 39, 72, 92)


# youngest_cricketer = min(Sakib, Mushfiq, Mustafiz, Riyad)

# print(f'The youngest cricketer is {youngest_cricketer.name}')


# a=2250
# b=3600
# c=1000

# total=int(a+b+c)

# print(total)


class Akib:
    def init__(self,name,id,email):
        self.name=name
        self.id=id
        self.email=email
        
    def details(self):
        print(f"Name: {self.name}, ID: {self.id}, Email: {self.email}")
        
obj1=Akib("Suny",20221,"test@hotmail.com")
print(obj1.id)        



obj1="hello"
obj2="\tworld"
total=obj1 + obj2
print(total) 