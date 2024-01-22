class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is not None:
        print(root.value, end=" ")  # Process the current node
        preorder_traversal(root.left)  # Traverse the left subtree
        preorder_traversal(root.right)  # Traverse the right subtree

def inorder_traversal(root):
    if root is not None:
        print(root.value, end=" ")  # Process the current node
        preorder_traversal(root.left)  # Traverse the left subtree
        preorder_traversal(root.right)  # Traverse the right

def postorder_traversal(root):
    if root is not None:
        print(root.value, end=" ")  # Process the current node
        preorder_traversal(root.left)  # Traverse the left subtree
        preorder_traversal(root.right)  # Traverse the right

# Example usage:
# Constructing a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Performing preorder traversal
print("Preorder Traversal:")
preorder_traversal(root)
