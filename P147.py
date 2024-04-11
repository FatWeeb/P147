from tkinter import *

root = Tk()
root.title("Project")

root.geometry("400x400")
root.configure(background = "light yellow")

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.3, anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg = "light yellow" , fg= "black")
label.place(relx=0.5, rely=0.7, anchor=CENTER)

label1 = Label(root, text = "Name in Encrypted Form : ", bg = "light yellow" , fg= "black")
label1.place(relx=0.5, rely=0.8, anchor=CENTER)

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label1["text"] += str(chr(encrypted))
        
btn = Button(root, text = "Show", command = asciiConverter, bg = 'yellow', fg = 'black')
btn.place(relx=0.5, rely= 0.5, anchor=CENTER)

root.mainloop()