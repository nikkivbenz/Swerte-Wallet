from tkinter import *

#tkk? 

#base for all frames
root = Tk()
root.title("Swerte Wallet")
root.geometry('350x200')

startWindowFrame = Frame(root)     
learnMoreFrame = Frame(root)


def startWindow(): 
    learnMoreFrame.pack_forget()
    startWindowFrame.tkraise()
    welcomeText = Label(startWindowFrame, text = "Welcome to Swerte Wallet")
    welcomeText.grid(row = 0, column = 2)    

    createAccountButton = Button(startWindowFrame, text = "Create a XLM Account", command = createAccount)
    createAccountButton.grid(row = 2, column = 2)

    reloadAccountButton = Button(startWindowFrame, text = "Load an existing XLM Account", command = loadAccount)
    reloadAccountButton.grid(row = 4, column = 2)

    learnMoreButton = Button(startWindowFrame, text = "Learn more about Swerte Wallet", command = learnMore)
    learnMoreButton.grid(row = 6, column = 2)
    startWindowFrame.pack()
    

def learnMore(): 
    startWindowFrame.pack_forget()
    learnMoreFrame.tkraise()
    aboutXLMText = Label(learnMoreFrame, text = "This wallet supports the storage of XLM from the Stellar Lumens Foundation")
    aboutXLMText.grid(row = 0, column  = 2)

    functionalitiesText= Label(learnMoreFrame, text = "Here, you can create a new Stellar Lumens account or load up an existing one.")
    functionalitiesText.grid(row = 3, column = 2) 

    backToStartButton = Button(learnMoreFrame, text = "Back to Main Page", command = startWindow)
    backToStartButton.grid(row = 5, column = 2) 
    learnMoreFrame.pack()
    

def createAccount():
    pass

def loadAccount(): 
    pass
def clicked(): 
    pass


startWindow()
root.mainloop()
