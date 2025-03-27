#Encryption Program


import random
import string


chars=" "+string.punctuation+string.digits+string.ascii_letters
#chars şifreleme için kullancağımız karakterleri gösteriyor

#print(chars)

chars=list(chars)
# list yaptık çünkü tek tek element olmasını istiyoruz

key=chars.copy() # copies chars to key

random.shuffle(key)    #her seferinde yeniden yapıyor

print(f"chars:{chars}")
print(f"key  :{key}")

#ENCRYPT

plain_text=input("enter a message to encrypt: ")
cipher_text= ""


for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f"original message is {plain_text}")
print(f"encrypted message is {cipher_text}")


#DECRYPT

cipher_text=input("enter a message to encrypt: ")
plain_text= ""


for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]

print(f"encrypted message is {cipher_text}")
print(f"original message is {plain_text}")








