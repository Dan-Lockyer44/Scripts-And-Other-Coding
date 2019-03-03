import os
import sys
from colorama import init ###Used to call the colour library
from termcolor import colored

init()

print(" ")
print(" ")
print(" ")
print(colored('======================================================================================================', 'red', 'on_white'))
print(colored('                                                                                                      ', 'white', 'on_white'))
print(colored('                                                                                                      ', 'white', 'on_white'))
print(colored('                This Crypto Generator Is Currently A WIP; Created By Daniel Lockyer                   ', 'green' , 'on_white'))
print(colored('                                                                                                      ', 'white', 'on_white'))
print(colored('                                                                                                      ', 'white', 'on_white'))
print(colored('======================================================================================================', 'red', 'on_white'))
print(" ")
print(" ")
print(" ")

toencrypt = input("Please Enter Some Text To Encrypt: ") ###Used to obtain the text to be encrypted
cipherkey = input("Please Insert An Encryption Key Made Of Numbers Only (Please Use 2 Or More Numbers): ") ###Used to obtain the encryption key

def pause():
    programPause = input("Press the ENTER key to continue...")
    restart_program()

def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):

    order = {
        int(val): num for num, val in enumerate(key)
    }

    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue

    return ciphertext

print("       ")
print(colored("Here is your encrypted text:", 'yellow', 'on_blue'))
print(encode(cipherkey, toencrypt))

def restart_program():
    ###Restarts the entire script
    python = sys.executable
    os.execl(python, python, * sys.argv)
if __name__ == "__main__":
    print("")
    print("")
    answer = input("Do you want to restart this program ? ")
    if answer.lower().strip() in "y yes".split():
        restart_program()
    else:
        print("Exiting, Goodbye")
