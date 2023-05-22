birthday_dict = {
    "Hen Hatuka": "30.10.2001",
    "Ori Uziel": "5.12.2001"
}

print("welcome to the bithday dictionary. we know the birthday of:")
for keys, value in birthday_dict.items():
   print(keys)
name = input("pick a name to check the birthday ")
print(birthday_dict[name])