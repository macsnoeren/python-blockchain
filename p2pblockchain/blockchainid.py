import os
import json

"""
Author: Maurice Snoeren <macsnoeren(at)gmail.com>
Version: 0.1 beta (use at your own risk)
Date: 26-06-2021
"""

class BlockchainId:

    def __init__(self, file_blockchain_id="blockchain.id"):
        """BlockchainId constructor. This class implements the blockchain id that holds all the important information."""

        self.file_blockchain_id = file_blockchain_id

        self.data = {}

        if os.path.isfile(file_blockchain_id):
            self.read_file_blockchain_id()

        else:
            self.create_file_blockchain_id()

    def read_file_blockchain_id(self):
        try:
            with open(self.file_blockchain_id, 'r') as file:
                self.data = json.loads( file.read() )
                print(self.data)

        except FileNotFoundError:
            print("read_file_blockchain_id: The file is not present.")

        except:
            print("read_file_blockchain_id: Error processing blockchain id file.")

    def create_file_blockchain_id(self):
        self.data = {"id": input("give your id: ")}

        try:
            f = open(self.file_blockchain_id, "w")
            f.write( json.dumps(self.data) )
            f.close()

        except Exception:
            print("create_file_blockchain_id: Writing file failed.")

    def get_id(self):
        return self.data["id"]