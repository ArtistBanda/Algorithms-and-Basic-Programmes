class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


def insertBST(root, value):
    if root == None:
        root = Node(value)

    else:
        if value < root.value:
            if root.right is None:
                root.right = Node(value)
            else:
                insertBST(root.right, value)

        else:
            if root.left is None:
                root.left = Node(value)
            else:
                insertBST(root.left, value)


def preorderTraversal(root):

    if root == None:
        return
    print(root.value, end=' ')
    preorderTraversal(root.left)
    preorderTraversal(root.right)


def inorderTraversal(root):

    if root == None:
        return
    inorderTraversal(root.left)
    print(root.value, end=' ')
    inorderTraversal(root.right)


def postorderTraversal(root):

    if root == None:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.value, end=' ')

# Test Code


root = Node(4)
insertBST(root, 2)
insertBST(root, 1)
insertBST(root, 3)
insertBST(root, 4)
insertBST(root, 5)
insertBST(root, 6)
print('Preorder Traversal : ', end='')
preorderTraversal(root)
print()
print('Inorder Traversal : ', end='')
inorderTraversal(root)
print()
print('Postorder Traversal : ', end='')
postorderTraversal(root)
print()
