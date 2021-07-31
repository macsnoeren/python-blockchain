"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 31-07-2021
"""

class ConsensusAlgorithm:

    def __init__(self, dir_blockchain="blockchain", consensus_algorithm=None):
        """This class implements the base class of the consensus algorithm. When you implement the consensus algorithm,
           please derive from this class."""

        self.name = "Base class consensus algorithm"

