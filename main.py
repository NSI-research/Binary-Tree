# -------------------
#
#   Auteur : Lodjo28
#   Nom du fichier : main
#   Version : 0.1
#
# -------------------

class TreeNode:

    def __init__(self, value):
        self.value = value  # On défini la valeur mère
        self.left = None  # On dit qu'il n'y a rien à gauche
        self.right = None  # On dit qu'il n'y a rien à droite

    def insert(self, value):
        if value < self.value:
            if not self.left:  # Si il n'y a rien à gauche on créer un node à gauche
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:  # Si il n'y a rien à droite on créer un node à droite
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

tree = TreeNode(5)
tree.insert(5)
tree.insert(9)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(1)
tree.insert(4)

tree.inorder_traversal()