#password
# 5 letters at least    should include . and first letter is upper letter


password = input("enter ur password: ")

while True:
        if  len(password)<5 or not password[0].isupper() or "." not in password:

            password=input("enter your password again: ")
        else:
            break

print("you set your password correctfully.")