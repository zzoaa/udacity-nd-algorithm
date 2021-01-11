import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return "{} {} {}".format(self.timestamp, self.data, self.hash)


class BlockChain(object):

    def __init__(self):
        self.blocks = []

    def add(self, data):
        prev_hash = None
        if self.blocks:
            prev_hash = self.blocks[-1].hash

        self.blocks.append(Block(time.gmtime(), data, prev_hash))

    def print_all(self):
        for block in self.blocks:
            print(block)


def main():
    blocks = BlockChain()

    blocks.add("1")
    blocks.add("2")
    blocks.add("3")

    blocks.print_all()


main()
