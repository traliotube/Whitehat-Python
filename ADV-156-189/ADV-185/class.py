import hashlib
from simplecrypt import encrypt, decrypt

value = "Hello"
hexString = ""


def SHA256():
    result = hashlib.sha256(value.encode())
    print(f"SHA256: ", result.hexdigest())


SHA256()


def MD5():
    result = hashlib.md5(value.encode())
    print("MD5: ", result.hexdigest())


MD5()


def encryption():
    global hexString
    cipherCode = encrypt("password", value)
    hexString = cipherCode.hex()
    print(f"Encryption: {hexString}")


def decryption():
    global hexString
    byteStr = bytes.fromhex(hexString)
    original = decrypt("password", byteStr)
    finalMessage = original.decode("utf-8")
    print(f"Decryption: {finalMessage}")


encryption()
decryption()
