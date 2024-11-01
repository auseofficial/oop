import datetime 
today= datetime.datetime.today()
print(today)

# import turtle
# turtle.circle(50)
# turtle.done()

# class Car:
#     name="Range Rover"
#     color="Black"
    
#     def start():
#         print("Rebel time stars now")

# print("Name of the car :",Car.name)
# print("Color of the car :",Car.color)        

# Car.start()


# class Walton:
#     digiTech=""
#     hiitech=""
    
#     def start():
#         print("Nazrul is the CEO")
        
# Walton.digitech="Software Engineer"
# Walton.hitech="Hardware Engineer"
# print("Working at :",Walton.digitech)
# print(Walton.hitech)

# Walton.start()
        
        
        
# class Car:
#     color="red"
#     brand="toyota"
    
#     def start():
#      print("Lets start the car") 
     
# print("Color of the car :",Car.color)
# print("Brand of the car :",Car.brand)

# Car.start()            

# class Student:
#     name="Akib Us Suny Eshan"
    
# s1 = Student()
# print(s1)    

# s2= Student()
# print(s2)

# class Car:
#     name="Totota"
#     color="Red"
    
# car1= Car()
# print(car1.name)
# print(car1.color)


# class Car:
#     def __init__():
#         print("Adding new elements in database ")
#     name="Totota"
#     color="Red"
 
# print()   

# class Car:
#     def __init__(self):
#         print(self)
#         print("Adding new elements in database ")

    
# car1= Car()
# print()

# class Car:
#     def __init__(self,fullname):
#         self.fullname=fullname
#         print("Adding new elements in database ")

    
# s1= Car("by Eshan")
# print(s1.fullname)

# class Car:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("Adding new elements in database ")

    
# s1= Car("by Eshan",99)
# print(s1.name,s1.marks)

# s2= Car("by Eshan",00)
# print(s2.name,s2.marks)


# class Car:
#     college_name="Notre Dame College"
    
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("Adding new elements in database ")
    
#     def welcome(self):
#         print("Welcome student :",self.name)
            
#     def get_marks(self):
#         print("Here is the marks :",self.marks)  
              
# s1= Car("Here is your google classroom",00)
# s1.welcome()
# print(s1.welcome())


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
            

# "Abstruction"
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started..")
        
car1=Car()
car1.start()        
            

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_num = acc

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Tk.", amount, "was debited")
            print("Total balance:", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Tk.", amount, "was credited")
        print("Total balance:", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(1000, 12345)
acc1.debit(1000)
acc1.credit(500) 