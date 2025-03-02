class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def verify_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.value == q.value) and self.verify_same_tree(p.left, q.left) and self.verify_same_tree(p.right, q.right)