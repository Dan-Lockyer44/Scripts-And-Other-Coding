import os
import sys
from colorama import init, Style ###Used to call the colour library
from termcolor import colored
init()

def main_menu():
    print("Please Choose A Number From One Of The Following: ")
    print(colored(Style.BRIGHT + "1. Encrypt Plain Text", 'green'))
    print(colored(Style.BRIGHT + "2. Decrypt Plain Text", 'blue'))



main_menu()

choice = input("Enter Choice Here: ")



def transpositioncode():

    init()

    print(" ")
    print(" ")
    print(" ")
    print(colored('======================================================================================================', 'red', 'on_white'))
    print(colored('                                                                                                      ', 'white', 'on_white'))
    print(colored('                                                                                                      ', 'white', 'on_white'))
    print(colored('                This Crypto Generator Is Currently A WIP; Created By Daniel Lockyer                   ', 'green' , 'on_white'))
    print(colored(Style.BRIGHT + '                                              ENCRYPTION                                              ', 'magenta' , 'on_white'))
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


if choice =='1':
    transpositioncode()
    if choice =='2':
        print("Decryption Code Goes Here")
    else:
        print("Please Enter A Valid Number")
