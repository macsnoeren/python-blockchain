import os
from datetime import datetime, timezone
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

class Transaction:

    def __init__(self, initiator, t="transaction", data={}):
        """This class implements one transaction that changes the state of the blockchain."""

        self.transaction_types = ["participant", "smartcontract", "transaction"]

        if not t in self.transaction_types:
            raise NameError("Transaction type can only be participant, smartcontract or transaction.")

        if not type(data) is dict:
            raise TypeError("Transaction data must be of type dict.")

        self.transaction = {
            "initiator"    : initiator,
            "data"         : data,
            "type"         : t,
            "timestamp"    : datetime.now(timezone.utc).isoformat(),
        }

        # Create an id of the transaction
        self.transaction["id"] = SHA256.new( json.dumps(self.transaction, sort_keys=True).encode('utf-8') ).hexdigest()

    def sign_transaction(self, signature):
        self.transaction["signature"] = signature

    def __str__(self):
        return "Transaction: \n" + json.dumps(self.transaction, sort_keys=True, indent=2)
