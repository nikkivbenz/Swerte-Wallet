import sqlite3

#dropCreateAccountsTable = "DROP TABLE userAccounts "
#curObjsor.execute(dropCreateAccountsTable)

class UserDatabase():         

    def getCursorObj(self): 
        usersDB = sqlite3.connect("userDB.db")
        return usersDB.cursor()

    def dropAccountTable(self): 
        #drops then creates for a new slate of information
        pass


    def addAccount(self, publicKey, privateKey):


        insertAccount1 = "INSERT INTO userAccounts(email, password) values('yes', 'HI')"
        self.cursorObj.execute(insertAccount1)

    def createAccountsTable(self): 

        createAccountsTable = "CREATE TABLE userAccounts(email STRING, password STRING)"
        self.cursorObj.execute(createAccountsTable) 



    def closeDatabase(self): 
        self.usersDB.close()



def main(): 
    uD = UserDatabase()
    getAccount = "SELECT * from userAccounts" 
    accounts = (uD.getCursorObj()).execute(getAccount)

    for a in accounts: 
        print(a)

    uD.closeDatabase()


main()