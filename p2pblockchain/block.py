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

from p2pblockchain.transaction import Transaction

"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 30-07-2021
"""


class Block:

    def __init__(self, block=None, previous_block=None, transactions=[]):
        """Block constructor. This class implements one block with all the transactions."""

        self.block = {
            "hash_previous_block": 0x00,
            "transactions": transactions,
            "height": 0
        }

        if previous_block != None:
            self.block["hash_previous_block"] = previous_block.block["hash"]
            self.block["height"] = previous_block.block["height"] + 1

        if block != None:
            self.block = block

        self.update_block_hash()

    def update_block_hash(self):
        if "hash" in self.block:
            del self.block["hash"]

        line = json.dumps(self.block, sort_keys=True)
        hash = SHA256.new(line.encode('utf-8'))
        self.block["hash"] = hash.hexdigest()

        return hash

    def add_transaction(self, transaction):
        self.block["transactions"].append(transaction.transaction)
        self.update_block_hash()

    def check_block(self):
        # TODO: check the hash_previous_block, transaction array and height and check the hash
        return True

    def __str__(self):
        return "Block: \n" + json.dumps(self.block, sort_keys=True, indent=2)
