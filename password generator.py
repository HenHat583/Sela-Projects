import secrets

print("WELCOME TO PASSWORD GENERATOR")
answer = int(input("how many characters to you want for your password? "))
print (secrets.token_hex(answer))