"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 31-07-2021
"""

from datetime import datetime, timezone
from random import randrange

from p2pblockchain.consensus_algorithm import ConsensusAlgorithm
from p2pblockchain.block import Block


class ProofOfWork(ConsensusAlgorithm):
    '''This class implements the proof-of-work algorithm for the blockchain, just likt bitcoin does.'''

    def __init__(self):
        """This class implements the concrete implementation of the consensus algorithm proof-of-work."""

        super(ConsensusAlgorithm, self).__init__()

        self.name = "Consensus algorithm Proof-of-Work"

        self.difficulty = 2 ** 16  # default difficulty. TODO: Needs to be changed according to some rules.

    def mine_block(self, block: Block):
        '''Find the hash by changing the nonce value for this block using the difficulty.'''
        block.block["timestamp"] = datetime.now(timezone.utc).isoformat()
        block.block["difficulty"] = self.difficulty
        block.block["nonce"] = randrange(2 ** 256)
        block.update_block_hash()

        while int(block.block["hash"], 16) > (2 ** 256 / self.difficulty):
            block.block["nonce"] = randrange(2 ** 256)
            block.update_block_hash()

    def check_block(self, block: Block):
        '''Check if the proof-of-work of this block is correct. TODO: The difficulty can be different
           for each block, so we need to calculate the difficulty for the particular block.'''
        return not (int(block.block["hash"], 16) > (2 ** 256 / self.difficulty))
