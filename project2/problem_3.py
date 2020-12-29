import sys
from heapq import heappush, heappop


class Node(object):

    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __str__(self):
        return "({},{})".format(self.char, self.freq)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented

        return self.freq == other.freq and self.char == other.char

    def __lt__(self, other):
        return self.freq < other.freq


def make_char_freq(data):
    result = {}

    for char in data:
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1

    return result


def huffman_encoding(data):
    queue = PriorityQueue()

    [queue.add(node) for node in table_to_nodes(make_char_freq(data))]
    huffman_tree = HuffmanTree.from_queue(queue)

    huffman_tree.build_encoded_data()
    return huffman_tree.encode(data), huffman_tree


def huffman_decoding(data, tree):
    return tree.decode(data)


def test(a_great_sentence):
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


def testing(expected, actual):
    print("Pass" if expected == actual else "Fail : {} but {}".format(expected, actual))


def table_to_nodes(table):
    return [Node(freq=table[key], char=key) for key in table]


class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    def add(self, node):
        heappush(self.queue, node)

    def pop(self):
        return heappop(self.queue)

    def size(self):
        return len(self.queue)


class HuffmanTree(object):

    def __init__(self, node):
        self.root = node
        self.encoded_data = {}
        self.cursor = None

    @classmethod
    def from_queue(cls, queue):
        while queue.size() > 1:
            left = queue.pop()
            right = queue.pop()
            parent = Node(left.freq + right.freq)
            parent.left = left
            parent.right = right
            queue.add(parent)

        return HuffmanTree(queue.pop())

    def build_encoded_data(self):
        self.__pre_order(self.root)

    def __pre_order(self, node, prefix_code=''):

        if node.left:
            self.__pre_order(node.left, prefix_code+'0')

        if node.right:
            self.__pre_order(node.right, prefix_code+'1')

        if node.left is None and node.right is None:
            self.encoded_data[node.char] = ''.join(prefix_code)

    def encode(self, sentence):
        return ''.join([self.encoded_data[char] for char in sentence])

    def decode(self, data):
        result = []
        self.cursor = self.root

        for char in data:
            if char == '0':
                self.cursor = self.cursor.left

            elif char == '1':
                self.cursor = self.cursor.right

            if self.cursor.left is None and self.cursor.right is None:
                result.append(self.cursor.char)
                self.cursor = self.root

        return ''.join(result)


def testing_pop_out(queue):
    testing(queue.pop(), Node(freq=2, char='D'))
    testing(queue.pop(), Node(freq=3, char='B'))

    queue.add(Node(5))

    testing(queue.pop(), Node(freq=5))
    testing(queue.pop(), Node(freq=6, char='E'))

    queue.add(Node(11))

    testing(queue.pop(), Node(freq=7, char='A'))
    testing(queue.pop(), Node(freq=7, char='C'))

    queue.add(Node(14))

    testing(queue.pop(), Node(freq=11))
    testing(queue.pop(), Node(freq=14))


def printing(message):
    print("*" * 30)
    print(message)
    print("*" * 30)


if __name__ == "__main__":
    codes = {}

    chars = "AAAAAAABBBCCCCCCCDDEEEEEE"

    table = make_char_freq(chars)

    testing(table['A'], 7)
    testing(table['D'], 2)

    nodes = table_to_nodes(table)

    testing(sorted(nodes, key=lambda x: x.freq)[0], Node(freq=2, char='D'))

    printing("testing_pop_out")
    queue = PriorityQueue()
    [queue.add(node) for node in nodes]
    testing_pop_out(queue)

    printing("testing_build_tree")
    queue = PriorityQueue()
    [queue.add(node) for node in nodes]

    huffman_tree = HuffmanTree.from_queue(queue)
    testing(huffman_tree.root, Node(25))

    huffman_tree.build_encoded_data()

    testing(huffman_tree.encoded_data['D'], '000')
    testing(huffman_tree.encoded_data['B'], '001')
    testing(huffman_tree.encoded_data['E'], '01')
    testing(huffman_tree.encoded_data['A'], '10')
    testing(huffman_tree.encoded_data['C'], '11')

    testing(huffman_tree.encode(chars), '1010101010101000100100111111111111111000000010101010101')
    testing(huffman_tree.decode('1010101010101000100100111111111111111000000010101010101'), chars)

    test(a_great_sentence="The bird is the word")
