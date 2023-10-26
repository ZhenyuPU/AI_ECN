from Contents import contents

# constants
modulo = chr(256)
huffman_maker = 257

class HuffmanTreeNode:
    def __init__(self, symbol = None, num = None):
        # un noeude
        self.symbol = symbol   # symbole
        self.weight = num    # weights
        self.g = None
        self.d = None
        self.buffers = []
    
    def merge(self, nodes: list):
        # nodes est une liste dont chaque element est huffmantreenode
        # en ordre descente
        nodes.sort(key=lambda node:node.weight, reverse=True)
        # print(f"第{i}次，{nodes[-1]}, {nodes[-2]}")
        n = HuffmanTreeNode(num=(nodes[-1].weight + nodes[-2].weight))
        n.g = nodes.pop(-1)
        n.d = nodes.pop(-1)
        nodes.append(n)
        return
        
    
    def less(self, a, b) -> bool:
        if a.weight < b.weight:
            return True
        return False
    

    def build_codemap_rec(self, code, codemap: dict):
        # ajouter dans la liste codemap par un symbole
        # code initial []
        # en ordre prefixe
        # au milieu
        if self.symbol:
            codemap[self.symbol] = code
            return
        # a gauche
        self.g.build_codemap_rec(code + [0], codemap)
        # a droite
        self.d.build_codemap_rec(code + [1], codemap)

    
class Huffman:
    huffman_marker = 259
    def __init__(self):
        # un pointeur vers None
        # en pratique, declarer qu'il pointe vers la racine
        # l'attribut tree fait référence à un objet de la classe HuffmanTreeNode 
        self.tree = HuffmanTreeNode()
        self.codes = {}

    def build_tree(self, text: list):
        weights = {}
        for item in text:
            if item in weights:
                weights[item] += 1
            else:
                weights[item] = 0

        weights[self.huffman_marker] = 1
        nodes = [HuffmanTreeNode(k, v) for k, v in weights.items()]
        # Sortie en ordre inverse
        # -1 et -2 sont le dernier plus petit et le deuxième plus petit
        while len(nodes) != 1:
            self.tree.merge(nodes)
        self.tree = nodes[0]
        return self.tree
        
        
    def build_codemap(self):
            if self.tree:
                code = []
                self.tree.build_codemap_rec(code, self.codes)
            return self.codes
        
    def encode(self, codemap):
        encoded_data = []
        buffer = 0
        count_bit = 0
        for item in codemap:
            for bit in codemap[item]:
                buffer = (buffer << 1) | bit
                count_bit += 1
                if count_bit == 8:
                    encoded_data.append(buffer.to_bytes(1, byteorder='big'))
                    count_bit = 0
                    buffer = 0
        
        return encoded_data
    
    def decode(self, encoded_data):
        decoded_text = ""
        current_node = self.tree
        bit = 0
        bits = []
        for byte in encoded_data:
            byte_value = int.from_bytes(byte, byteorder='big')  # 将字节数组解码为整数
            for i in range(7, -1, -1):
                bit = (byte_value >> i) & 1
                bits.append(bit)
        
        for bit in bits:
            if bit == 0:
                current_node = current_node.g
            elif bit ==1:
                current_node = current_node.d
                
            if current_node.g is None and current_node.d is None:
                # leaf
                decoded_text += str(current_node.symbol)
                current_node = self.tree
        return decoded_text
    """
    1. 第一个符号的编码方式是依照符号的编码长度给予相同长度的'0'值
    2. 对接下来的符号的编码+1，保证接下来的编码大小都大于之前
    3. 如果编码较长，比特左移一位并补0
    """
    def heapsort(self, A):
        n = len(A)
        for i in range(n // 2, -1, -1):
            self.heap_fix_down_max(A, i, n)

    def heap_fix_down_max(self, A, i, n):
        largest = i
        left = 2* i + 1
        right = 2*i + 2
        if left < n and A[left] > A[largest]:
            largest = left
        if right < n and A[right] > A[largest]:
            largest = right
        if left < n and right < n and A[left] == A[right] and A[left] > A[largest]:
            if A.keys(A[left]) < A.keys(A[right]):
                largest = right
            else:
                largest = left
    
    def canonical_diffs(self):
        # trier le codemap
        # codemap 最上面的最小
        # tri par tas
        self.heapsort(self.codes)
        # 取位数
        c = {}
        codes = self.codes
        keys = list(codes.keys())
        for i in range(len(self.codes)):
            if i == 0:
                c[keys[0]] = 0 * len(keys)
            else:
                if len(codes[keys[i]]) == len(codes[keys[i-1]]):
                    c[keys[i]] = c[keys[i-1]] + 1
                else:
                    c[keys[i]] = c[keys[i-1]] + 1
                    c[keys[i]] << 1
        i = 0
        l = []
        for item in c:
            if i % 2 == 0:
                l.append(item)
            else:
                l.append(c[item])
        return l

    def build_canonical_codemap(self, l):
        self.codes = [None] * (huffman_maker + 1)
        for i in range(0, len(l), 2):
            self.codes[l[i]] = l[i+1]
        return self.codes
    
    # i initial 0
    def rebuild_tree_rec(self, i):
        l = self.canonical_diffs()
        if i >= len(l):
            return
    
        if i % 2 == 0:
            self.tree.weight = l[i+1]
            self.tree.symbol = l[i]
        
        self.tree.g.rebuild_tree_rec(i+2)
        self.tree.d.rebuild_tree_rec(i+2)

    def build_tree(self):
        i = 0
        self.build_tree_rec(i)
        return self.tree
    
    def split_symbols(self, l):
        for i in range(0, len(l)-1, 2):
            if l[i] > 255:
                l[i+1] = 0
                l[i] = modulo
    
    def merge_symbols(self, l):
        codes = {}
        # j 记录堆最左边的indice
        j = 1
        codes[l[0]] = 0
        i = 0
        while i < len(l) - 1:
            m = 0
            if i // 2 == 2 * (j-1) + 1:

                while (2**j >= m):
                    codes[l[i]] = [0] + []
                    i += 1
            j += 1


def binary_list(x):
    n = len(x)
    q0 = x
    q1 = q0 // 2
    res = []
    while q1 > 0:
        a = q0 - q1 * 2
        res.append(a)
    return res



if __name__ == "__main__":
    file = "pg5097.txt"
    text = contents(file)
    #text = text.decode('utf-8')
    tree = Huffman()
    tree.build_tree(text)
    codemap = {}
    codemap = tree.build_codemap()
    encoded_data = tree.encode(codemap)
    decoded_data = tree.decode(encoded_data)
    print(decoded_data)

    
    


