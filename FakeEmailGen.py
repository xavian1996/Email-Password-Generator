import random
from time import sleep

class EmailGen:
    def GenerateEmail():
        lines = open("male-names.txt").read().splitlines()
        return random.choice(lines)

    def GeneratePwd():
        lines = open("10-million-password-list-top-1000000.txt").read().splitlines()
        return random.choice(lines)
fname = EmailGen.GenerateEmail()
lname = EmailGen.GenerateEmail()
pwd = EmailGen.GeneratePwd()
pwd1 = EmailGen.GeneratePwd()
print("""


 ____  __    _  _  ____    ____  __  __    __    ____  __       ___  ____  _  _ 
( ___)/__\  ( )/ )( ___)  ( ___)(  \/  )  /__\  (_  _)(  )     / __)( ___)( \( )
 )__)/(__)\  )  (  )__)    )__)  )    (  /(__)\  _)(_  )(__   ( (_-. )__)  )  ( 
(__)(__)(__)(_)\_)(____)  (____)(_/\/\_)(__)(__)(____)(____)   \___/(____)(_)\_)

Coded By Xavian1996
""")
print('[+] Starting Executing The Script .')
print('[+] Generating Email ! Please Wait 2sec .')
sleep(2)
print(f"[+] Email => {fname}.{lname}@gmail.com")
print(f"[+] Password => {pwd}{pwd1}")
print('[+] Finished Executing The Script.')
exit()
