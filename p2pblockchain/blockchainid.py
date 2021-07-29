import os
import datetime
import json
import hashlib
import base64
import getpass

# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 26-06-2021
"""

class BlockchainId:

    def __init__(self, file_blockchain_id="blockchain.id"):
        """BlockchainId constructor. This class implements the blockchain id that holds all the important information.
           It could be seen as some kind of wallet. This class will be used to create an identification on the blockchain
           and store it safely in a file. When the user starts the node again, a password is required to unlock the
           wallet."""

        self.file_blockchain_id = file_blockchain_id

        self.data = {}

        if os.path.isfile(file_blockchain_id):
            self.read_file_blockchain_id()

        else:
            self.create_file_blockchain_id()

    def read_file_blockchain_id(self):
        '''This method reads the blockchain id file to get the information. The file is
            encrypted, so the user needs to provide the password to unlock the file. When
            successfull, the method returns True, otherwise False.'''
        try:
            f = open(self.file_blockchain_id, "r")
            salt      = base64.b64decode( f.readline() )
            iv        = base64.b64decode( f.readline() )
            encrypted = base64.b64decode( f.readline() )
            f.close()

            password  = getpass.getpass("Enter the password to open your wallet: ")
            key       = hashlib.scrypt(bytes(password, 'utf-8'), salt=salt, n=1024, r=8, p=1, dklen=32) # derive a 32 byte key = 256 bit
            cipher    = AES.new(key, AES.MODE_CBC, iv=iv)
            decrypted = unpad( cipher.decrypt(encrypted), AES.block_size )

            self.data = json.loads(decrypted)
            return True

        except FileNotFoundError:
            print("read_file_blockchain_id: The file is not present.")

        except:
            print("read_file_blockchain_id: Wrong password?!")

        return False

    def create_file_blockchain_id(self):
        '''When no blockchain id file exist, the file needs to be created. All the 
           initial information is created for the user. The created file is protected
           by a password that is provided by the user. Make sure, it is a strong 
           password and that you do not lose it!'''

        print("You need to create your wallet for the blockchain.")
        name = input("What is your name: ")
        password1 = getpass.getpass("Enter a password to protect your identification: ")
        password2 = getpass.getpass("Re-enter your password: ")

        if password1 != password2:
            print("Passwords do not match!")
            
        else:
            # Derive a key from the password to increase entropy!
            salt      = os.urandom(32)
            key       = hashlib.scrypt(bytes(password1, 'utf-8'), salt=salt, n=1024, r=8, p=1, dklen=32) # derive a 32 byte key = 256 bit
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            id        = hashlib.sha3_512( bytes( str(salt)+str(key)+str(timestamp)+str(name), 'utf-8') ).hexdigest()

            self.data = { "created": timestamp, "name": name, "id": id, "key_signing": self.create_key(), "key_encryption": self.create_key() }

            cipher    = AES.new(key, AES.MODE_CBC)
            encrypted = cipher.encrypt(pad(bytes( json.dumps(self.data), 'utf-8'), AES.block_size))

        try:
            f = open(self.file_blockchain_id, "w")
            f.write( str(base64.b64encode(salt).decode('utf-8')) + "\n" )
            f.write( str(base64.b64encode(cipher.iv).decode('utf-8')) + "\n" )
            f.write( str(base64.b64encode(encrypted).decode('utf-8')) + "\n" )
            f.close()
            
        except Exception as e:
            print("create_file_blockchain_id: Writing file failed: " + str(e))

    def create_key(self, type='ECC-P-256'):
        '''Generic method to creata a key. Default ECC-P-256! Nothing else is implemented at this
           moment. Default behavior is to create a key with the highest security. This class uses
           the method to create al the necessary keys for encryption and signing purposes.'''
        key = ECC.generate(curve='P-256')
        return { "type": "ECC-P-256", "PEM": key.export_key(format='PEM') }

    def get_signing_key(self):
        '''Returns the private and public key that has been generated for the signing process.'''
        return ECC.import_key(self.data["key_signing"]["PEM"]) # TODO: Only implemented type is ECC-256, but this should be checked.

    def get_signing_key_public(self):
        '''Returns only the public key that has been generated for the signing process.'''
        key = self.get_signing_key()
        return key.public_key()#.export_key(format='PEM')

    def get_encryption_key(self):
        '''Returns the private and public key that has been generated for the encryption process.'''
        return ECC.import_key(self.data["key_encryption"]["PEM"]) # TODO: Only implemented type is ECC-256, but this should be checked.

    def get_encryption_key_public(self):
        '''Returns only the public key that has been generated for the encryption process.'''
        key = self.get_encryption_key()
        return key.public_key()#.export_key(format='PEM')

    def sign_message(self, message):
        '''Sign the given message with the generated key for the signing process.
           TODO: If the message is a dict it should be transformed based on alphabet => new method hash_message(self, message)'''
        key = self.get_signing_key()
        h = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        signature = signer.sign(h)
        return base64.b64encode(signature).decode('utf-8')

    def verify_signature(self, message, signature, key):
        '''Verify the signature based on the message, signature and public key.'''
        signature = base64.b64decode(signature)
        h = SHA256.new(message)
        verifier = DSS.new(key, 'fips-186-3')

        try:
            verifier.verify(h, signature)
            return True

        except ValueError:
            return False

    def get_public_identification(self):
        '''Returns the public information that everybody should know. It should be
           on the blockchain as well.'''
        return { "created": self.data["created"],
                 "name": self.data["name"],
                 "id": self.data["id"],
                 "key_signing": self.get_signing_key_public().export_key(format='PEM'),
                 "key_encryption": self.get_encryption_key_public().export_key(format='PEM')
                }

    def is_valid(self):
        '''Returns True when the identification is valid, otherwise False.'''
        return "id" in self.data

    def get_id(self):
        '''Returns the id assiociated with the current identification (or user).'''
        return self.data["id"]