# https://medium.com/@ashiqgiga07/asymmetric-cryptography-with-python-5eed86772731
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
import base64
import os

class CriptoServer:  
    def __init__(self):
        if not os.path.exists('./keys'):    
            os.mkdir('./keys')
        
        self._pr_path = f"./keys/private_key.pem"
        self._pu_path = f"./keys/public_key.pem" 
      
        if not os.path.isfile(self._pr_path):
            # create keys
            pr_key = RSA.generate(1024)
            pu_key = pr_key.publickey()
            pr_pem = pr_key.export_key().decode()
            pu_pem = pu_key.export_key().decode()
            with open(self._pr_path, 'w') as pr:
                pr.write(pr_pem)
            with open(self._pu_path, 'w') as pu:
                pu.write(pu_pem)

        self._pr_key = RSA.import_key(open(self._pr_path, 'r').read())        
        self._decrypt = PKCS1_OAEP.new(key=self._pr_key)

    def Decript(self, message:str):
        base64_bytes = message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return self._decrypt.decrypt(message_bytes).decode('ascii')

class CriptoClient:
    def __init__(self):
        self._pu_path = f"./keys/public_key.pem" 
        if not os.path.isfile(self._pu_path):
            raise Exception(f"We need a public key on {self._pu_path} to continue")

        self._pu_key = RSA.import_key(open(self._pu_path, 'r').read())
        self._cipher = PKCS1_OAEP.new(key=self._pu_key)

    def Encript(self, message:str):
        encrypt = self._cipher.encrypt(message.encode('ascii'))
        base64_bytes = base64.b64encode(encrypt)
        return base64_bytes.decode('ascii')