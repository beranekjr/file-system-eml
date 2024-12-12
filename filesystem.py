import utils
from directory import Directory

class FyleSystem:
    def __init__(self, root='root'):
        self.root = root
        self.current = root
        self.contents = utils.LinkedList()
        self.blocks = utils.HashTable()

    def createDir(self, name):
        try:
            dir = Directory(name)
            self.blocks.set(name, dir)
            self.contents.append(dir)

            print(f"Directory '{name}' created successfully")
        except utils.HashKeyAlreadyExist:
            print("Directory already exists")