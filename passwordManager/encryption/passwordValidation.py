import hashlib
from distutils.log import error


def checkValid(password, hash):
    try:
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        if hash == hashedPassword:
            return True

        return False

    except:
        error("[ERROR] make sure passowrd is valid")
        return False

def createHash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generateKeys(hash):
    pass

def hashPasswords(password, publicKey):
    pass

def getPassword(hash, privateKey):
    pass