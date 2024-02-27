from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    ciphertext=ciphertext.decode("iso-8859-1")
  
    filenameforcipher="cipher.txt"
    
    with open("cipher.txt","w") as f:
        f.write(ciphertext)
def decrypt(ciphertext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Decrypt the ciphertext and remove the padding
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print(decrypted_data.decode())
    #return decrypted_data
def filegenerator(filename,text):
    with open(filename,"wb") as f:
        #f.write(str(text,'UTF-8'))
        #f.write(text.decode())
        f.write(text)
def menu():
    print("")
    print("")
    print("1. ENCYPTION USING AES ALGORITHM")
    print("2. DECRYPTION USING AES ALGORITHM")
    print("")
    print("")
    n=int(input())
    if n==1:
        #encrypted_data = encrypt(plaintext, key)
        #print("Encrypted data:", encrypted_data)
        key = get_random_bytes(32)  # Generating keys/passphrase
        filenameforkey="keyfile.txt"
        filegenerator(filenameforkey, key)
        #print(key)
        with open("keyfile.txt","rb") as f:
            key=f.read()
        
        plaintext = bytes(input("ENTER YOUR TEXT : "),'utf-8')
      
        encrypt(plaintext, key)

    elif n==2:
        #decrypted_data = decrypt(encrypted_data, key)
        #print("Decrypted data:", decrypted_data)
        with open("after.txt","r") as f:
            encrypted_data=f.read()
            
        with open("keyfile.txt","rb") as f:
            key=f.read()
        
        #print(key) 
        encrypted_data=bytes(encrypted_data,"iso-8859-1") 
      
        decrypt(encrypted_data, key)

menu()
