from stellar_sdk.keypair import Keypair

def createNewAccount(): 
    pair = Keypair.random()
    publicKey = pair.public_key
    privateKey = pair.secret

    #print(publicKey)
    #print(privateKey)

    return [publicKey, privateKey]

