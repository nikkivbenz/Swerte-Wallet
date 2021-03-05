import sqlite3

#dropCreateAccountsTable = "DROP TABLE userAccounts "
#curObj.execute(dropCreateAccountsTable)

class UserDatabase(): 
    def __init__(self):
         pass
        

def acccountTable(): 
    #drops then creates for a new slate of information
    pass


def addAccount(publicKey, privateKey):


    insertAccount1 = "INSERT INTO userAccounts(email, password) values('yes', 'HI')"
    curObj.execute(insertAccount1)

def createAccountsTable(): 

    createAccountsTable = "CREATE TABLE userAccounts(email STRING, password STRING)"
    curObj.execute(createAccountsTable) 


#close at end 
def open(): 

    usersDB = sqlite3.connect("userDB.db")
    curObj = usersDB.cursor()


def main(): 
    getAccount = "SELECT * from userAccounts" 
    accounts = curObj.execute(getAccount)

    for a in accounts: 
        print(a)


#usersDB.close()