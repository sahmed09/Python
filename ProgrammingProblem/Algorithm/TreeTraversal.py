"""
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root)

Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)

Algorithm Preorder(tree)
   1. Visit the root.
   2. Traverse the left subtree, i.e., call Preorder(left-subtree)
   3. Traverse the right subtree, i.e., call Preorder(right-subtree)

Algorithm Postorder(tree)
   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
   3. Visit the root.
"""


# A class that represents an individual node in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        printInorder(root.left)  # First recur on left child
        print(root.val, end=" ")  # Then print the data of node
        printInorder(root.right)  # Now recur on right child


# A function to do inorder tree traversal
def printPostorder(root):
    if root:
        printPostorder(root.left)  # First recur on left child
        printPostorder(root.right)  # Then recur on right child
        print(root.val, end=" ")  # Now print the data of node


# A function to do inorder tree traversal
def printPreorder(root):
    if root:
        print(root.val, end=" ")  # First print the data of node
        printPreorder(root.left)  # Then recur on left child
        printPreorder(root.right)  # Finally recur on right child


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal of binary tree is")
    printPreorder(root)

    print("\nInorder traversal of binary tree is")
    printInorder(root)

    print("\nPostorder traversal of binary tree is")
    printPostorder(root)

    # Time Complexity: O(n)
