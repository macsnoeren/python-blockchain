from p2pnetwork.node import Node

from p2pblockchain.blockchain_id import BlockchainId
from p2pblockchain.blockchain import Blockchain
from p2pblockchain.proof_of_work import ProofOfWork

"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 26-06-2021
"""


class BlockchainNode(Node):

    def __init__(self, file_blockchain_id="blockchain.id", host="localhost", port=8000, consensus_algorithm=None):
        """BlockchainNode constructor."""

        self.blockchain_id = BlockchainId(file_blockchain_id)
        while not self.blockchain_id.is_valid():
            self.blockchain_id = BlockchainId(file_blockchain_id)

        if consensus_algorithm is None:
            consensus_algorithm = ProofOfWork()

        self.blockchain = Blockchain(consensus_algorithm=consensus_algorithm)

        super(BlockchainNode, self).__init__(host, port, self.blockchain_id.get_id())
        print("BlockchainNode: Started")

    def outbound_node_connected(self, node):
        print("outbound_node_connected (" + self.id + "): " + node.id)

    def inbound_node_connected(self, node):
        print("inbound_node_connected: (" + self.id + "): " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: (" + self.id + "): " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: (" + self.id + "): " + node.id)

    def node_message(self, node, data):
        print("node_message (" + self.id + ") from " + node.id + ": " + str(data))

    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: (" + self.id + "): " + node.id)

    def node_request_to_stop(self):
        print("node is requested to stop (" + self.id + "): ")
