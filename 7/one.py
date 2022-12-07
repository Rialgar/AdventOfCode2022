import functools
import re

class Entry:
    def __init__(self, name:str):
        self.name: str = name
        self.parent: Directory = None

    def getSize(self) -> int:
        return 0


class File(Entry):
    def __init__(self, name:str, size:int):
        Entry.__init__(self, name)
        self.size: int = size

    def getSize(self) -> int:
        return self.size

class Directory(Entry):
    def __init__(self, name:str):
        Entry.__init__(self, name)
        self.children: dict[str, Entry] = {}
        self.cachedSize: int = None

    def getSize(self) -> int:
        if self.cachedSize == None:
            self.cachedSize = functools.reduce(lambda sum, child: sum + child.getSize(), self.children.values(), 0)
        return self.cachedSize

    def addChild(self, child: Entry):
        self.children[child.name] = child
        child.parent = self
        self.cachedSize = None


root = Directory('/')
allDirectories = [root]
currentDir = root

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        if line == '$ cd /\n' :
            currentDir = root
        elif line == '$ cd ..\n':
            # we assume that all the navigations in the log worked
            currentDir = currentDir.parent
            # print(currentDir.name)
        else:
            cd_command: re.Match = re.match('\$ cd (.+)', line)
            if cd_command :
                dir = Directory(cd_command.group(1) + '/')
                currentDir.addChild(dir)
                currentDir = dir
                # print(currentDir.name)
            else:
                file_output: re.Match = re.match('([0-9]+) (.+)', line)
                if(file_output):
                    file = File(file_output.group(2), int(file_output.group(1)))
                    currentDir.addChild(file)
                    # print(file.name, file.size)

sum = 0

def iterate(dir: Directory):
    global sum
    if dir.getSize() <= 100000:
        sum = sum + dir.getSize()
    for child in dir.children.values():
        if isinstance(child, Directory):
            iterate(child)

iterate(root)
        
print(sum)
