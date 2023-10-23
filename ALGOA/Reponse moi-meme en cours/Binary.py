
class TreeNode:
    def __init__ (self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__ (self):
        self.root = None
    
    def search(self, x):
        if self.root is None:
            return False
        
        cur = TreeNode()
        cur = self.root
        while cur:
            if cur.value < x:
                cur = cur.right
            elif cur.value > x:
                cur = cur.left
            else:
                return True
            
        return False
    
    def insert(self, x):
        new_node = TreeNode(value = x)
        if self.root is None:
            self.root = new_node
            return self.root
        tree = TreeNode()
        cur = TreeNode()
        tree = self.root
        while tree:
            if x < tree.value:
                cur = tree
                tree = tree.left
            elif x > tree.value:
                cur = tree
                tree = tree.right
        if x < cur.value:
            cur.left = new_node
        elif x >= cur.value:
            cur.right = new_node
        return self.root

    def del_tree(self, x):
        if self.root is None:
            return None
        
        tree = TreeNode()
        pre = TreeNode()
        tree = self.root
        while tree:
            if x < tree.value:
                pre = tree
                tree = tree.left
            elif x > tree.value:
                pre = tree
                tree = tree.right
            elif x == tree.value:
                if tree.left is None:
                    if pre.left == tree:
                        pre.left = tree.right
                    else:
                        pre.right = tree.right
                elif tree.right is None:
                    if pre.left == tree:
                        pre.left = tree.left
                    else:
                        pre.right = tree.left
                else:
                    # 在右子树找到最小的，这个值小于右子树的其他值而大于左子树的所有值
                    tree.value = find_min_value(tree.right)
                    # 删除右子树的这个值
                    parent = TreeNode()
                    parent = tree
                    tree = tree.right
                    while tree.left:
                        parent = tree
                        tree = tree.left
                    # print(tree.value)
                    if parent.right == tree:
                        parent.right = tree.right
                    else:
                        parent.left = tree.left
                return self.root

    
    # prefix
    def print_(self):
        root = TreeNode()
        root = self.root
        # pile = Pile()
        pile = []
        while root or pile:
            while root:
                pile.append(root)
                print(root.value)
                root = root.left
            root = pile.pop()
            root = root.right

    def print_tree(self):
        if self.root is None:
            return

        current = self.root
        stack = []  # 使用堆栈来模拟中序遍历

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.value)

            current = current.right

def find_min_value(A):
    if A.left is None:
        return A.value
    x = find_min_value(A.left)
    return x

if __name__ == '__main__':
    Tree = BinaryTree()
    Tree.insert(4)
    Tree.insert(1)
    Tree.insert(0)
    Tree.insert(2)
    Tree.insert(3)
    Tree.insert(6)
    Tree.insert(5)
    Tree.insert(7)
    Tree.insert(8)
    Tree.del_tree(6)
    Tree.print_()
    
    print(Tree.search(8))



            