import datetime
x = datetime.datetime.now()
name = input("please enter your name ")
age = input("please enter your age ")
try:
    int(age)
except:
    while type (age) is not int:
        try:
            int(age)
            break
        except:
            print ("ENTER A NUMBER NOT ANOTHER WORD YOU JUMBU >:-P")
            age = input("please enter your age ")
print(name+"," , "you will be 100 years old in" , (x.year) + 100 - int(age))
number = input("please enter a number(yabastard :)")
try:
    int(number)
except:
    while type (number) is not int:
        try:
            int(number)
            break
        except:
            print ("ENTER A NUMBER NOT ANOTHER WORD YOU JUMBU >:-P")
            number = input("please enter a number(yabastard :)")
for i in range (1,int(number)):
    print (name+"," , "you will be 100 years old in" , (x.year) + 100 - int(age))

#print(int(number) * (name+"," , "you will be 100 years old in" , (x.year) + 100 - int(age)))