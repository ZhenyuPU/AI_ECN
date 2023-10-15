from Contents import contents

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

    
    


