import socket
import time
import threading
import random
import hashlib

from p2pnetwork.node import Node
from p2pblockchain.blockchainid import BlockchainId

"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 26-06-2021
"""

class BlockchainNode(Node):

    def __init__(self, file_blockchain_id="blockchain.id", host="localhost", port=8000):
        """BlockchainNode constructor."""

        self.id = BlockchainId(file_blockchain_id)

        print(self.id.is_valid())

        print(self.id.get_id())

        super(BlockchainNode, self).__init__(host, port, self.id.get_id())
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
        