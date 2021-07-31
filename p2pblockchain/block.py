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

    def __init__(self, dir_blockchain="blockchain", consensus_algorithm=None):
        """Block constructor. This class implements one block with all the transactions."""

        self.block = {
            "hash_previous_block": "",
            "transactions"       : [],
            #timestamp    = "" # This should be always added when the block is closed
            #nonce        = "" # This should be is added by the consensus algo
            "hash"        : "" # This should be is added by the consensus algo
        }

        self.consensus_algorithm = consensus_algorithm

        if ( self.consensus_algorithm == None ):
            pass # Create here a the deafaul consesnus algorithm

    def update_block_hash(self):
        if "hash" in self.block:
            del self.block["hash"]

        line = json.dumps(self.block, sort_keys=True)
        hash = SHA256.new(line.encode('utf-8'))
        self.block["hash"] = hash

        return hash

    def add_transaction(self, transaction):
        self.block["transaction"].append(transaction.transaction)
        self.update_block_hash()