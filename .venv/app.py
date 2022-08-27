from re import I
import sqlite3

conn = sqlite3.connect('password.db')

MASTER_PASSWORD = 1234

password = input("Insert your password master:")
if not password.isnumeric():
        print("you need to enter a number")
        password = int(password)
if password != MASTER_PASSWORD:
    print("PASSWORD INVALID! CLOSED")
    exit()



cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def options():
   print('-=-'* 20)
   print("I : Insert new password")
   print("L : List saved services")
   print("R : Recover a password")
   print("R : Recover a password")
   print("S:  Go out")
   print('-=-'* 20)


while True:
    options()
    option = input("What do you want to do?")
    if option not in ["L","I","R","S"]:
        print("option invalid")
        continue

    if option == "S":
        break

conn.close()