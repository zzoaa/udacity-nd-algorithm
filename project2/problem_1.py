class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return "({},{})".format(self.key, self.value)


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


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.keys = DoubleLinkedList()
        self.map = {}

    def get(self, key):

        result = -1
        if key in self.map:
            node = self.map[key]

            if node.prev and node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
            elif node.next:
                node.next.prev = None
                self.keys.head = node.next
            else:
                return node.value

            tail_node = self.keys.get_tail()
            tail_node.next = node
            node.prev = tail_node
            node.next = None
            self.keys.tail = node

            result = node.value

        return result

    def set(self, key, value):
        node = Node(key, value)

        if self.size == self.capacity:
            node_of_lru = self.keys.pop()
            del self.map[node_of_lru.key]
            self.size = self.size - 1

        self.keys.append(node)
        self.map[key] = node
        self.size = self.size + 1

    def __str__(self):
        return str(self.map)


def test(actual, expected):
    result = "Pass" if expected == actual else "Fail expected:{}, but actual:{} ".format(expected, actual)
    print(result)


def iterate(head):

    current = head

    while current:
        print(current)
        current = current.next


def main():

    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    test(our_cache.get(1), 1)       # returns 1
    test(our_cache.get(2), 2)       # returns 2
    test(our_cache.get(9), -1)      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    test(our_cache.get(3), -1)


main()
