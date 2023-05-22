num = int(input("enter how many Fibonacci numbers you want "))
a = 0
b = 1
for i in range(num-2):
    c = a + b
    print(c)
    a = b
    b = c