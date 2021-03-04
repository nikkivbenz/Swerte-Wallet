from tkinter import *
import AccountFunctions as AF
#tkk? 

#base for all frames
root = Tk()
root.title("Swerte Wallet")
root.geometry('350x200')

startWindowFrame = Frame(root)     
learnMoreFrame = Frame(root)

#for create account
explanationFrame = Frame(root) 
createAccountFrame = Frame(root) 


def startWindow(): 
    learnMoreFrame.pack_forget()
    startWindowFrame.tkraise()
    welcomeText = Label(startWindowFrame, text = "Welcome to Swerte Wallet")
    welcomeText.grid(row = 0, column = 2)    

    createAccountButton = Button(startWindowFrame, text = "Create a XLM Account", command = createAccountInfo)
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
    

def createAccountInfo():
    startWindowFrame.pack_forget()

    #Information about how wallets work

    explanationFrame.tkraise()

    createAccountText = Label(explanationFrame, text = """Before we create a new account, you must know... 
    \nUpon creating a new XLM account in this wallet, you will be given two things: \n\nA public key and a private key \n\nA public key is your
    adddress where people can send you money, \n\nA private key is your secret key to accessing your account. Never share
    your private key with anyone. \n\nAs long as someone else has that key, they have access to your account.""")
    createAccountText.grid(row = 0, column = 2)

    understandButton = Button(explanationFrame, text = "I understand", command = createAccount)
    understandButton.grid( row = 2, column = 2)
    explanationFrame.pack()



def createAccount(): 
    explanationFrame.pack_forget()
    createAccountFrame.tkraise()


    #userKeyPair = AF.createNewAccount()
    

    public = "GDP3SFDLN3ZDA3FBBYC2M2SHJLVMWRFKHZX4WEN3YDF45EK2JE44V4GX"
    private = "SB7FNMFU7QMH6ZP66OISP5A4F5VAWOU2NYXMWBVKA76D2X36NGL2KA7X"


    accountCreatedText = Label(createAccountFrame, text = f"""Here is your account information: \nPublic Key:
    {public} \nPrivate Key: {private} """)
    accountCreatedText.grid(row = 0, column = 2)

    createAccountFrame.pack()
    

def loadAccount(): 
    pass
def clicked(): 
    pass


startWindow()
root.mainloop()
