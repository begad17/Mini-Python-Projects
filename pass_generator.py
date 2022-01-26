import string
from random import randint, choice

pass1 = string.ascii_letters + string.punctuation + string.digits

#All the characters that you can get
#print(pass1)

print("Pass"+"".join(choice(pass1) for x in range(8)))