#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (MyOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the MyOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################

import sys
import time
import argparse
sys.path.insert(0, '..') # Import the files where the modules are located

from p2pblockchain.blockchainnode import BlockchainNode

parser = argparse.ArgumentParser()
parser.add_argument("--wallet", "-w", help="The file that stores the blockchain identification/wallet. Default: blockchain.id", default="blockchain.id")
args = parser.parse_args()

node = BlockchainNode(file_blockchain_id=args.wallet)

node.start()

time.sleep(5)

node.stop()

print('end test')
