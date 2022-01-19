import json
import random


from datetime import datetime
from hashlib import sha256


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Create the genesis block
        print("Creating genesis block")
        self.new_block()

    def new_block(self):
        # Generates a new block and adds it to the chain
        block = {
            'index' : len(self.chain),
            'timestamp' : datetime.now().isoformat(),
            'transactions' : self.pending_transactions,
            'previous_hash' : self.last_block["hash"] if self.last_block else None,
            'nonce' : format(random.getrandbits(64), "x"),
        }

        block_hash = self.hash(block)
        block['hash'] = block_hash
        
        # Reset the list of pending transactions
        self.pending_transactions = []
        
        return block
    
    @staticmethod
    def hash(block):
        # Hashes a block
        # We ensure the dictionary is sorted or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Gets the latest block in the chain
        # Returns the last block in the chain (if there are blocks)

        return self.chain[-1] if self.chain else None

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of pending transactions
        self.pending_transactions.append({
            "recipient" : recipient,
            "sender" : sender,
            "amount" : amount,
        })

    def proof_of_work(self):
        count = 0
        while True:
            count += 1
            new_block = self.new_block()
            if self.valid_hash(new_block):
                break
        
        new_block['count'] = count
        print(f"new block found : {new_block}")
        self.chain.append(new_block)
        return new_block

    @staticmethod
    def valid_hash(block):
        # checks wheather or not the hash generated is valid or not
        # for example here we check that the hash should start with '0000'
        return block['hash'].startswith('0000')


# (1/210000)BTC