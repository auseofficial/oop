# class Dog:
#   price= 1000
#   color= "red"
#   location="dhaka"
  
# my_dog= Dog()

# print(my_dog)
# print(my_dog.price)
# print(my_dog.color)   
# print(my_dog.location)   
       
       

# class Dog:
#   price= 1000
#   color= "red"
#   location="dhaka"       


class Student:
  roll = ""
  gpa  = ""

  def __init__ (self,roll,gpa):
    self.roll=roll
    self.gpa=gpa

  def display(self):
     print(f"Roll : {self.roll}, GPA :{self.gpa}")
    
rahim = Student(101,5.00)
rahim.display()

karim = Student(101,5.00)
karim.display()