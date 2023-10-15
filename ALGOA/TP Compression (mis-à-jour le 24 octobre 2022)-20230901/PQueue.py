class PQueue:
    def __init__(self):
        self.headlist = [0]   # il reste 0
        self.size = 0

    def insertion(self, node):
        self.headlist.append(node)
        self.size += 1
        i = self.size
        while i // 2 > 0:
            if self.headlist[i] < self.headlist[i // 2]:
                self.headlist[i], self.headlist[i // 2] = self.headlist[i // 2], self.headlist[i]
            i = i // 2
    
    def extract_min(self):
        self.headlist[1] = self.headlist[self.size]
        self.headlist[1], self.headlist[2] = self.headlist[2], self.headlist[1]
        self.size -= 1
        self.headlist.pop()
        i = 2
        while i <= self.size:
            if self.headlist[i * 2] <= self.headlist[i * 2 + 1]:
                if self.headlist[i] > self.headlist[i * 2]:
                    self.headlist[i], self.headlist[i * 2] = self.headlist[i * 2], self.headlist[i]
            else:
                if self.headlist[i] > self.headlist[i * 2 + 1]:
                    self.headlist[i], self.headlist[i * 2 + 1] = self.headlist[i * 2 + 1], self.headlist[i]
            i = i * 2
    
    def file_size(self):
        size = len(len(self.headlist)) - 1
        return size