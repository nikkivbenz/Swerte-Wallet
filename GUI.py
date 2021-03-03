from tkinter import *


#root window
root = Tk()
root.title("Swerte Wallet")
root.geometry('350x200')


#menu @ top

def startWindow(): 
    startMenu = Label(root, text = "Welcome to Swerte Wallet")
    startMenu.grid(row = 0, column = 1)    
    createAccountButton = Button(root, text = "Create a XLM Account", command = createAccount)
    createAccountButton.grid(row = 2, column = 1)

    reloadAccountButton = Button(root, text = "Load an existing XLM Account", command = loadAccount)
    reloadAccountButton.grid(row = 4, column = 1)

    learnMoreButton = Button(root, text = "Learn more about Swerte Wallet", command = learnMorePage)
    learnMoreButton.grid(row = 6, column = 1)


def learnMorePage(): 
    pass
def createAccount():
    pass

def loadAccount(): 
    pass
def clicked(): 
    pass







startWindow()
root.mainloop()

