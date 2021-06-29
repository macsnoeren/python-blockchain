# Module python-blockchain

A Python implementation of a blockchain using the module p2pnetwork. This is a from scratch implemented blockchain. It is aimed to have the same features as Ethereum. Implementing smart contracts using the Python language. Its purpose is for education and research.

## Design

A blockchain is a peer-to-peer application that uses a decentralized ledger that is shared among all the nodes. This ledger can be read by anyone. Off course you can implement aspects of hiding sensitive information. The design is as follows:
1. The blockchain node is the "wallet" of the user.
2. When started from scratch, the node will prompt the user to create a blockchain identification. This is a unique id (auto generated), public and private key (also auto generated). The id and the public key is send to the blockchain network. On the disk a blockchain.id file is stored containing the id and private key. This file will be password protected. Note that mechanism to recover the private key could be implemented. 
3. When the user is logged into the node, it downloads the blockchain ledger. It already participates within the network and update the blockchain ledger. The blockchain ledger is downloaded from the newest entry. Multiple nodes can be used/asked to download the ledger from.
4. The blockchain node, will create multiple connections with the network, based on discovery. 