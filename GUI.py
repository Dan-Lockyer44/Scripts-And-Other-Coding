import tkinter as tk #Importing the gui module
import os
import sys
from colorama import init, Style ###Used to call the colour library
from termcolor import colored

class Application(tk.Frame):
    def __init__(self, master=None): #Creating the main window for the buttons on the gui
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.transposition_button = tk.Button(self) #Creating the first button for the transposition cipher
        self.transposition_button["text"] = "Transposition Cipher" #Giving the button some text
        self.transposition_button["command"] = self.transposition #Giving the button a use, once clicked goes to the transposition function
        self.transposition_button.pack(side="top") #Used to format where the transposition button goes

        self.quit = tk.Button(self, text="QUIT", fg="red") #Giving the button a command to exit the program
        self.quit["command"] = self.end
        self.quit.pack(side="bottom") #Used to format where the quit button goes

        self.other = tk.Button(self)
        self.other["text"] = "Other"
        self.other["command"] = self.test
        self.other.pack(side="top")

    def end(self):
        sys.exit()
    def transposition(self):
        init() #used to "start" colorama

        def main_menu():
            print("Please Choose A Number From One Of The Following: ") #Used to bring up the selection menu for the transposition cipher
            print(colored(Style.BRIGHT + "1. Encrypt Plain Text", 'green'))
            print(colored(Style.BRIGHT + "2. Decrypt Plain Text", 'blue'))


        main_menu() #Used to call the function main_menu to get the user to select an option

        choice = input("Enter Choice Here: ") #Used to capture the user's selection



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

            toencrypt = input("Please Enter Some Text To Encrypt: ") #Used to obtain the text to be encrypted
            cipherkey = input("Please Insert An Encryption Key Made Of Numbers Only (Please Use 2 Or More Numbers): ") #Used to obtain the encryption key

            def pause():
                programPause = input("Press the ENTER key to continue...")
                restart_program() #Used to pause and restart the program, not currently implemented

            def split_len(seq, length): #Used to get the length of the inputted text
                return [seq[i:i + length] for i in range(0, len(seq), length)]

            def encode(key, plaintext):

                order = {
                    int(val): num for num, val in enumerate(key) #Used to create the cipher
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
            print(colored("Here is your encrypted text:", 'yellow', 'on_blue')) #Used to output the final encrypted text
            print(encode(cipherkey, toencrypt))

            def restart_program(): #Used to restart the program once the text has been encrypted
                #Restarts the entire script
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


        if choice =='1': #used at the start of the script to validate user input and run a module depending on the user's input
            transpositioncode()
            if choice =='2':
                print("Decryption Code Goes Here")
            else:
                print("Please Enter A Valid Number")



    def test(self):
        print("This Code Is Yet To Be Implemented Please Watch This Space")



root = tk.Tk()
app = Application(master=root)
app.mainloop() #Used to make the gui stay visible
