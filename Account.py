import CreateWallet
def main(): 
    menu()
    
def menu(): 
    print("\nWelcome! What would you like to do?")
    print("1. Create a Wallet")
    print("2. Load a Wallet")
    print("3. Unsure")
    try: 
        userChoice = int(input("\nPlease Enter a Number: "))
        if userChoice == 1: 
            #CreateWallet.main
            pass
    except ValueError as e: 
        print("Please enter a valid value.")
        menu()



main()