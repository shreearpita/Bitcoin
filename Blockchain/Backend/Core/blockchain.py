import sys
sys.path.append('#')

from .block import Block
from .blockheader import BlockHeader
from ..util.util import hash256
import time

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()

    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
         timestamp = int(time.time())
         Transaction = f"Kakashi sent {BlockHeight} Bitcoins to Goku"
         merkleRoot = hash256(Transaction.encode()).hex()
         bits = 'ffff001f'
         blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
         blockheader.mine()
         self.chain.append(Block(BlockHeight, 1, blockheader, 1, Transaction))
         print(self.chain)


if __name__ == "__main__":
    blockchain = Blockchain()
