class N:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def branchSumsPreOrder(root):
    a = []
    branchSumsHelper(root, a, 0)
    return a

def branchSumsHelper(node, a, curSum):
    if node is None:
        return

    curSum += node.val

    if node.left is None and node.right is None:
        a.append(curSum)

    branchSumsHelper(node.left, a, curSum)
    branchSumsHelper(node.right, a, curSum)

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = N(1), N(2), N(3), N(4), N(5), N(6), N(7), N(8), N(9), N(10)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7
n4.left, n4.right = n8, n9
n5.left = n10

print(branchSumsPreOrder(n1))