# Code created and published by: Harsh Patel

class Node:
    def __init__(self, name, isFile=False):
        self.name = name
        self.isFile = isFile
        self.children = {}
        self.parent = None

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class FileSystem:
    def __init__(self):
        self.root = Node("root")
        self.currentDir = self.root
        self.path_head = LinkedListNode(self.root)
        self.path_tail = self.path_head

    def mkdir(self, dirname):
        if dirname in self.currentDir.children:
            print("Directory already exists")
            return
        new_dir = Node(dirname)
        new_dir.parent = self.currentDir
        self.currentDir.children[dirname] = new_dir
        print(f"Directory '{dirname}' created")

    def touch(self, filename):
        if filename in self.currentDir.children:
            print("File already exists")
            return
        new_file = Node(filename, isFile=True)
        new_file.parent = self.currentDir
        self.currentDir.children[filename] = new_file
        print(f"File '{filename}' created")

    def ls(self):
        return list(self.currentDir.children.keys())

    def cd(self, path):
        if path == "..":
            if self.currentDir != self.root:
                self.path_tail = self.path_tail.prev
                self.currentDir = self.path_tail.data
            return
        if path not in self.currentDir.children:
            print("No such directory")
            return
        if not self.currentDir.children[path].isFile:
            self.currentDir = self.currentDir.children[path]
            new_node = LinkedListNode(self.currentDir)
            self.path_tail.next = new_node
            new_node.prev = self.path_tail
            self.path_tail = new_node
        else:
            print("Not a directory")
            
    def print_absolute_path(self):
        current = self.path_tail
        path = ""
        while current:
            path = "/" + current.data.name + path
            current = current.prev
        return path


def main():
    fs = FileSystem()
    while True:
        command = input(f"{fs.print_absolute_path()}> ")
        if command == "exit":
            break
        elif command == "ls":
            result = fs.ls()
            print(f"\n\tDirectory: {fs.print_absolute_path()}\n")
            for key in result:
                print(key)
        elif command.startswith("mkdir"):
            dirname = command.split(" ")[1]
            fs.mkdir(dirname)
        elif command.startswith("cd"):
            path = command.split(" ")[1]
            fs.cd(path)
        elif command.startswith("touch"):
            filenames = command.split(" ")
            filenames.remove("touch")
            for eachFile in filenames:
                fs.touch(eachFile)

if __name__ == "__main__":
    main()


# Code created and published by: Harsh Patel