a=7
b=5
c=a
a=b
b=c
print(a)
print(b)
########password#############
print("------------PASSWORD-----------")
import random
import string

length = int(input("Enter Password Length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)