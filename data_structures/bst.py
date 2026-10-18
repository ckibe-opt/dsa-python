class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    """Binary search tree (no balancing)."""

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)
        # duplicates are ignored

    def contains(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def preorder(self):
        result = []

        def walk(node):
            if node:
                result.append(node.key)
                walk(node.left)
                walk(node.right)

        walk(self.root)
        return result

    def height(self):
        def h(node):
            if node is None:
                return 0
            return 1 + max(h(node.left), h(node.right))

        return h(self.root)

    def min(self):
        node = self.root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.key


if __name__ == "__main__":
    tree = BST()
    for k in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(k)
    print("inorder :", tree.inorder())
    print("preorder:", tree.preorder())
    print("height  :", tree.height())
