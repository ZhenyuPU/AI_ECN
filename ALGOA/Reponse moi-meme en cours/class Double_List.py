class Double_List:
    def __init__(self, item):
        self.d = item
        self.prev = None
        self.n = None
  
    def is_empty(self):
        return self.d == None or self.n ==None
  
    def insert_after(self, x, L):
        L_x = Double_List(x)
        if L.n == None:
            L.n = L_x.prev
            print(L.d)
            L_x.n = None
        return
        self.insert_after(x, L.n)
  
    def insert_before(self, x, L):
        L_x = Double_List(x)
        L_x.n = L.n
        L = L_x

if __name__ == '__main__':
    list = Double_List(5)
    for i in range(1, 9):
        list.insert_after(i, list)
    