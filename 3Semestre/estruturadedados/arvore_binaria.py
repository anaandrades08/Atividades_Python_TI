class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

#Função para ordenar a árvore
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

# Função para desenhar a árvore
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

# Valores a serem inseridos na árvore
values = [33, 15, 8, 60, 81, 7, 6, 5]

root = None

# Inserindo os valores na árvore
for value in values:
    root = insert(root, value)

# Imprimindo a árvore em ordem
print("Árvore em ordem:")
inorder_traversal(root)

print("------------------------------------")

# Imprimindo a árvore
print_tree(root)