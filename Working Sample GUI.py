from tkinter import *         ##Simple GUI Box




def f1():
    win = Tk()
    frame = Frame(win)
    canvas = Canvas(frame, width=600, height=400, bg='#aaaaff')
    frame.pack()
    canvas.pack()
    win.title('Hello User!')

    labelfont = ('times', 20, 'bold')
    widget = Label(win, text='Hello config world')
    widget.config(bg='black', fg='yellow') ##bg is background, fg is foreground
    widget.config(font=labelfont)
    widget.config(height=3, width=20)
    widget.pack(expand=YES, fill=BOTH)

    mylabel = Label(win,text="I am a label widget")
    mybutton = Button(win,text="I am a button")
    mylabel.pack()
    mybutton.pack()


    win.mainloop()      ##Used to make the GUI stay visable until it's closed by the user




def f2():
    parent = Tk()
    lbl = StringVar()
    lbl.set("Hello World")
    Label(parent, textvariable=lbl, bg='blue', fg="white", text=lbl).pack()
    parent.title('TEST PROGRAM')

    
    def toggle_text():
        """Toggle Button Text Between Hi and Goodbye"""
        if button["text"] == "ON":
            ##Switches to off
            button["text"] = "OFF"
            button.configure(bg="red")

        else:
            ##Reset to on
            button["text"] = "ON"
            button.configure(bg="green")

    button = Button(parent, text="ON", width=12, fg='white', bg='green', command=toggle_text)
    button.pack(padx=100, pady=10)

    chk_me = BooleanVar()

    def ch_callback():
        print(chk_me.get())

    Checkbutton(parent, text='Remember Me', variable=chk_me, command=ch_callback).pack()

    Entry(parent, width=30).pack()
    
    
    def ShowChoice(c):
        print(c.get())
        lbl.set(c.get())


    LANG = [
        ("Python", "Big Data"),
        ("c#", "GUI"),
        ("Swift", "IOS Mobile"),
        ("Kotlin", "Android Mobile"),
        ]
    v = StringVar()
    v.set("Please select an option")

    def lbl_callback(*args):
        print("variable Changed!", args)

    v.trace("w", lbl_callback)

    for language, mode in LANG:
        b = Radiobutton(parent, text=language,
                        variable=v, value=mode,command=lambda n=v: ShowChoice(n))
        b.pack(anchor=W)
        
    







if __name__ == '__main__':
    #f1()
    f2()
    
