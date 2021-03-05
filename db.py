import sqlite3

usersDB = sqlite3.connect("userDB.db")

curObj = usersDB.cursor()

dropCreateAccountsTable = "DROP TABLE userAccounts "
curObj.execute(dropCreateAccountsTable)


createAccountsTable = "CREATE TABLE userAccounts(ema STRING, password STRING)"
curObj.execute(createAccountsTable)

insertAccount1 = "INSERT INTO userAccounts(ema, password) values('yes', 'HI')"
curObj.execute(insertAccount1)

getAccount = "SELECT * from userAccounts" 
accounts = curObj.execute(getAccount)

#close at end 

for a in accounts: 
    print(a) 
    
usersDB.close()

