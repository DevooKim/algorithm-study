#전위 순회: NLR
def preOrder(node):
    if node is node:
        return

    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

#중위 순회: LNR
def inOrder(node):
    if node is None:
        return

    inOrder(node.left)
    print(node.val)
    inOrder(node.right)

#후위 순회: LRN
def postOrder(node):
    if node is None:
        return

    postOrder(node.left)
    postOrder(node.right)
    print(node.val)