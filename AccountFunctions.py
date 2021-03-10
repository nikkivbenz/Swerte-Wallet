from stellar_sdk.keypair import Keypair

#public = "GDP3SFDLN3ZDA3FBBYC2M2SHJLVMWRFKHZX4WEN3YDF45EK2JE44V4GX"
#private = "SB7FNMFU7QMH6ZP66OISP5A4F5VAWOU2NYXMWBVKA76D2X36NGL2KA7X"
def createNewAccount(): 
    pair = Keypair.random()
    publicKey = pair.public_key
    privateKey = pair.secret

    #print(publicKey)
    #print(privateKey)

    return [publicKey, privateKey]

def getAccountBalance(): 
    pass


def getPublicKeyFromSecret(secretKey): 
    public = Keypair.from_secret(secretKey)
    return public.public_key


def sendXLM(): 
    pass

def receieveXM(): 
    #shows public address the be received at 
    pass