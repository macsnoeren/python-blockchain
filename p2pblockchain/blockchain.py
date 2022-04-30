import os

from p2pblockchain.block import Block
from p2pblockchain.consensus_algorithm import ConsensusAlgorithm
from p2pblockchain.proof_of_work import ProofOfWork

# pip install tinyec
# pip install pycryptodome: https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html
# Interessant: https://cryptobook.nakov.com/asymmetric-key-ciphers/ecc-encryption-decryption

"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 30-07-2021
"""


class Blockchain:

    def __init__(self, dir_blockchain="blockchain", consensus_algorithm: ConsensusAlgorithm = ProofOfWork):
        """Blockchain constructor. This class implements the blockchain ledger with all the blocks."""

        self.blockchain = []

        self.blockchain_file = dir_blockchain + "/blockchain.dat"

        self.consensus_algorithm = consensus_algorithm

        if not os.path.isdir(dir_blockchain):
            os.mkdir(dir_blockchain)

        if os.path.isfile(self.blockchain_file):
            self.read_blockchain_file()

        else:
            try:
                f = open(self.blockchain_file, "w")
                f.close()

            except Exception as e:
                raise Exception("Could not create the blockchain file")

    def read_blockchain_file(self):
        pass

    def mine_block(self, block: Block):
        return self.consensus_algorithm.mine_block(block)

    def check_block(self, block: Block):
        return (block.check_block() and self.consensus_algorithm.check_block(
            block))  # TODO: and smart_contract.chech_block => participant
