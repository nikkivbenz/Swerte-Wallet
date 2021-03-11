from stellar_sdk import Keypair, Server, TransactionBuilder, Network, Asset

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


def sendXLM(secret, toAddress): 
    server = Server(horizon_url="https://horizon-testnet.stellar.org")
    source_keypair = Keypair.from_secret(secret)

    source_account = server.load_account(account_id=source_keypair.public_key)

    transaction = TransactionBuilder(
        source_account=source_account, network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE, base_fee=100) \
        .append_path_payment_strict_receive_op(destination=toAddress,
                                send_code="XLM", send_issuer=None, send_max="1000", dest_code="XLM",
                                dest_amount="5.50", path=path) \
        .set_timeout(30) \
        .build()
    transaction.sign(source_keypair)
    response = server.submit_transaction(transaction)

def receieveXM(): 
    #shows public address the be received at 
    pass







