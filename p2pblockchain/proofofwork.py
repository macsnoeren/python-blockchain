"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 31-07-2021
"""

from consensusalgorithm import ConsensusAlgorithm

class ProofOfWork(ConsensusAlgorithm):

    def __init__(self, dir_blockchain="blockchain", consensus_algorithm=None):
        """This class implements the concrete implementation of the consensus algorithm proof-of-work."""

        self.name = "Consensus algorithm Proof-of-Work"

