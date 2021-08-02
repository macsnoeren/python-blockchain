# Module python-blockchain

Blockchain is a very promosing combination of technologies. Providing a ledger system that can be trusted. This kind of technologies we need for the future, to become more resilient against cyber crime and identity theft. While blockchain already shown us good usage, like crypto coins and smart contract, it is still under development. The current implementation of most blockchains require large computing power to solve the difficult digital puzzles to provide trust. A lot of pools provide these computing power. It uses a lot of energy and is not sustainable for the future. Another drawback is the speed of the blockchain. A lot of things to fix. Blockchain can still become one of the technologies the Internet will be based upon. Up to a better and safer digital world!

This Python module provides a blockchain implementation. To implement the peer-to-peer node, it uses the Python module p2pnetwork (https://github.com/macsnoeren/python-p2p-network). This is a from scratch implemented blockchain purely in Python and it's aims to have the same features as Ethereum. Like the implementation of smart contracts using the Python language. Finally, the purpose of this module is for educational and research use. Use it at your own risk, when you use it for real world applications.

## Basic idea

A blockchain requires a basic functionality. The following basic functionality will be implemented:
- The blockchain node is implemented by the class BlockchainNode. This class extends the Node class of p2pnetwork. It creates a thread for the server and immediatly accept connections from other nodes.
- Every participant of the blockchain has an identity and a wallet to securely store this identity. Within this blockchain all participants must become public. If you create an account on this blockchain, it will be added to the blockchain. Everyone knows your public key and are able to validate your signatures immediatly. The class BlockchainId implements this functionality. The wallet is password protected. Make sure you use a strong password.
- The ledger of the blockchain is off course open and can hold anything you like. The basic ledger is implemented by the class Blockchain. This ledger contains the blocks, which is implemented by the class Block. The block contains transactions, which is implemented by Transaction. The Block class contains one or more transactions. Finally, the blockchain also requires a consensus algorithm. This could be a proof-of-work algorithm, like used by Bitcoin. It is also possible to use other types of consensus algorithms. The consensus algorithm will add some extra information to the block, like nonce value and a timestamp for example.
- While the blockchain is able to support smart contract, it will already implement three types of transactions:
    1. A special transaction "participant" adds a participant to the blockchain. From this moment, the participant is known and is able to participate with the network.
    2. A special transation "smartcontract", adds a smart contract to the blockchain. This smart contract can be used by the participant. Its methods can be called and result into transactions to change the state of the smart contract.
    3. The normal transaction "transaction" is used to change data on the blockchain. It uses the smart contracts that has been published on the blockchain and executes the code. The result of this code is pushed to the blockchain using transactions.

## Starting a blockchain node

It is easy to start a blockchain node. The following code creates a single node. 

```python
from p2pblockchain.blockchainnode import BlockchainNode

node = BlockchainNode()

node.start()

while 1==1:
    sleep(1000)
    # Do something
```


## Design
A blockchain is a peer-to-peer application that uses a decentralized ledger that is shared among all the nodes. This ledger can be read by anyone. Off course you can implement aspects of hiding sensitive information. The design is as follows:
1. The blockchain node is the "wallet" of the user.
2. When started from scratch, the node will prompt the user to create a blockchain identification. This is a unique id (auto generated), public and private key (also auto generated). The id and the public key is send to the blockchain network. On the disk a blockchain.id file is stored containing the id and private key. This file will be password protected. Note that mechanism to recover the private key could be implemented. 
3. When the user is logged into the node, it downloads the blockchain ledger. It already participates within the network and update the blockchain ledger. The blockchain ledger is downloaded from the newest entry. Multiple nodes can be used/asked to download the ledger from.
4. The blockchain node, will create multiple connections with the network, based on discovery. 