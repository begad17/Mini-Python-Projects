"""
Store and organize passwords
https://www.youtube.com/watch?v=DLn3jOsNRVE
"""
from cryptography.fernet import Fernet


def load_key():
    file = open("Key.key", "rb")
    key = file.read()
    file.close()
    return


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def view():
   #Add "pass" to avoid errors. does nothing
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, " Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    #w is to write but overrides, a to append (most flexible), r to read
    with open("passwords.txt", "a") as f:
        f.write(name + " " + fer.encrypt(pwd.encode()).decode()+ "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones? (View/Add). Q to quit").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
