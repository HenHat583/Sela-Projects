import random

s = "zxcvbnm,./asdfghjkl;'QWERTY1234567890-\,;lsf;!@#$%^&*()_+-=,./']\[]ZXVBNCXZNMVBN,MSDN,.GN;LASK;LJGLJKGHQWURPQIWRTIUPO"
passlen = int(input("how many characters to you want for your password? "))

p = "".join(random.sample(s,passlen ))
print (p)