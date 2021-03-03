from tkinter import *


#root window
root = Tk()
root.title("Swerte Wallet")
root.geometry('350x200')


#menu @ top
menu = Menu(root)
item = Menu(menu)

menu.add_cascade(label = 'File', menu = item)
item.add_command(label = 'New')
root.config(menu = menu)

def startWindow(): 
    startMenu = Label(root, text = "Welcome to Swerte Wallet")
    startMenu.grid()    

def clicked(): 
    pass





startWindow()
root.mainloop()

