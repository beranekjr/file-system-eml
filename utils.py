class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)

    def remove(self, data):
        current = self.head
        prev = None

        while current and current.data != data:
            prev = current
            current = current.next

        if not current:
            return False

        if not prev:
            self.head = current.next
        else:
            prev.next = current.next

        return True

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class HashKeyAlreadyExist(Exception):
    def __init__(self):
        super().__init__("Hash key already exists")

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range (size)]

    def __hash_key(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        hash_index = self.__hash_key(key)

        for idx, element in enumerate(self.table[hash_index]):
            if element[0] == key:
                raise HashKeyAlreadyExist()

        self.table[hash_index].append((key, value))

    def get(self, key):
        hash_index = self.__hash_key(key)

        for idx, element in enumerate(self.table[hash_index]):
            if element[0] == key:
                return element[1]

        return None
