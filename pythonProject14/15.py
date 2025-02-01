#password
# 5 letters at least    should include . first letter is upper letter

password=input("enter ur name")

while  len(password) >= 5 and password[0].isupper() and password.isalpha():
    print("not valide")
    name = input("enter ur name")

print(f"{password} valid")


#CALISMIYOE