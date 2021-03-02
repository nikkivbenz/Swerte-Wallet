from stellar_sdk.keypair import Keypair

def main(): 
    information()
    createKeys()

def createKeys():
    pair = Keypair.random()
    publickey = pair.public_key
    privatekey = pair.secret
    print("\nPublic Key: ", publickey)
    print("\nPrivate Key: ", privatekey)
    print("Write this down!")

def information(): 
    print("\nWelcome! Before we create your wallet, would you like to know more about wallets?")
    try: 
        userIn = int(input("Enter 1: 'Yes or 2: 'No'\n"))
        if userIn == 1: 
            print("\nWallets hold your crypto digitally. You will be given a public key and a private key.")
            input("\nPress Enter to continue...")
            print("\nA public key is an address that your family and friends can send you money to.")
            input("\nPress Enter to continue...")
            print("\nA private key is your way of accessing your account and funds. Guard this key!")
            input("\nPress Enter to continue...")
            print("\nAnyone with your private key can access your funds. ")
        elif userIn == 2: 
            print("Alright, making your account now!")
        else: 
            print("Enter a valid entry.")
            print("Trying Again...")
            input("\nPress Enter to continue...")
            information()
    except ValueError: 
        print('Please Enter a valid value. Trying Again...')
        information()

