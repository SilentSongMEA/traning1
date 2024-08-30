# try:
#   result=0
#   x=int(input('enter number'))
#   y=int(input('enter number'))
#   result=x /y
#   print(result)
# except ZeroDivisionError:
#   print('wrong')

# list1=[1,2,3,4,5,6,7,8,9,10]
# print(list1)

# list2=[]
# for i in range(1,11):
#   list2.append(i)
# print(list2)

# list3=[i for i in range(1,11)]
# print(list3)

# list4=[number for number in range(1,11) if number %2==0]
# print(list4)
# list5=[number*10 for number in range(1,11) if number %2==0]
# print(list5)

class person:
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
  def printname(self):
    print(self.firstname,self.lastname)
class student(person):
  def __init__(self,fname,lname,year):
    super().__init__(fname,lname)
    self.graduationyear=year
  def welcome(self):
    print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
x=student("mohi2","EA",2001)
x.welcome()
