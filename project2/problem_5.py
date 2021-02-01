import hashlib
import time


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return "({},{})".format(self.key, self.value)

    def __repr__(self):
        return "({} <- ({},{}) ->{})".format(self.prev, self.key, self.value, self.next)


class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def get_tail(self):
        return self.tail

    def pop(self):

        result = self.head
        self.head = result.next
        return result

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def __repr__(self):
        current = self.head
        result = []
        while current:
            result.append(current)
            current = current.next

        return "\n".join([str(item) for item in result])


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return "{} {} {}".format(self.timestamp, self.data, self.hash)


class BlockChain(object):

    def __init__(self):
        self.blocks = DoubleLinkedList()

    def add(self, data):
        prev_hash = None
        if self.blocks.get_tail():
            prev_hash = self.blocks.get_tail().hash

        self.blocks.append(Block(time.gmtime(), data, prev_hash))

    def print_all(self):
        print(self.blocks)


def main():
    blocks = BlockChain()

    blocks.add("1")
    blocks.add("2")
    blocks.add("3")

    blocks.print_all()
    print("="*10)

    blocks.add("4")
    blocks.add("5")
    blocks.add("6")
    blocks.add("4")
    blocks.add("5")
    blocks.add("6")
    blocks.add("4")
    blocks.add("5")
    blocks.add("6")
    blocks.add("4")
    blocks.add("5")
    blocks.add("6")

    blocks.print_all()
    print("=" * 10)

    blocks = BlockChain()
    blocks.print_all()
    print("=" * 10)

main()
