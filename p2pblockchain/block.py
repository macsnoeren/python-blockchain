import os
import datetime
import json
import hashlib
import base64
import getpass

# pip install tinyec
from tinyec import registry

# pip install pycryptodome: https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html
# Interessant: https://cryptobook.nakov.com/asymmetric-key-ciphers/ecc-encryption-decryption
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 30-07-2021
"""

class Block:

    def __init__(self, dir_blockchain="blockchain"):
        """Block constructor. This class implements one block with all the transactions."""

        self.transactions = {}

        #if os.path.isfile(file_blockchain_id):
        #    self.read_file_blockchain_id()

        #else:
        #    self.create_file_blockchain_id()

