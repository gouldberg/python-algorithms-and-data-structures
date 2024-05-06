# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Binary Trees
# ----------------------------------------------------------------------------

class BinaryTreeNode:

    def __init__(self, node_name=None, data=None, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right


# ----------
# create root = A
A = BinaryTreeNode(data=314, node_name='A')

# create other nodes
B = BinaryTreeNode(data=6)
C = BinaryTreeNode(data=271)
D = BinaryTreeNode(data=28)
E = BinaryTreeNode(data=0)
F = BinaryTreeNode(data=561)
G = BinaryTreeNode(data=3)
H = BinaryTreeNode(data=17)
I = BinaryTreeNode(data=6)
J = BinaryTreeNode(data=2)
K = BinaryTreeNode(data=1)
L = BinaryTreeNode(data=401)
M = BinaryTreeNode(data=641)
N = BinaryTreeNode(data=257)
O = BinaryTreeNode(data=271)
P = BinaryTreeNode(data=28)


A.left = B
B.left = C
C.left = D
C.right = E
B.right = F
F.right = G
G.left = H

A.right = I
I.left = J
J.right = K
K.right = N
K.left = L
L.right = M

I.right = O
O.right = P


# ----------------------------------------------------------------------------
# Tree Traversal with Recursion
# time complexity O(n) and space complexity O(h)
# ----------------------------------------------------------------------------

def tree_traversal(root):

    if root:
        # Preorder: visit the root, traverse the left subtree, then traverse the right subtree
        print('Preorder: %d' % root.data)
        tree_traversal(root.left)

        # Inorder: traverse the left subtree, visit the root, then traverse the right subtree
        print('Inorder: %d' % root.data)
        tree_traversal(root.right)

        # Postorder: traverse the left subtree, traverse the right subtree, and then visit the root
        print('Postorder: %d' % root.data)


# ----------
tree_traversal(A)

tree_traversal(C)

tree_traversal(H)


# ----------------------------------------------------------------------------
# Is balanced binary tree
# ----------------------------------------------------------------------------

import collections

def is_balanced_binary_tree(tree):

    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    # First value of the return value indicates if tree is balanced, and if balanced the second value of the return value
    # is the height of tree.

    def check_balanced(tree):
        if not tree:
            # Base case.
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced.
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced.
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


# ----------
# root A
is_balanced_binary_tree(A)

is_balanced_binary_tree(C)


# ----------------------------------------------------------------------------
# Is symmetric
# ----------------------------------------------------------------------------

def is_symmetric(tree):

    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data and
                    check_symmetric(subtree_0.left, subtree_1.right) and
                    check_symmetric(subtree_0.right, subtree_1.left))

        # One subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)


# ----------
is_symmetric(A)

is_symmetric(C)


# ----------------------------------------------------------------------------
# Sum of root-to-leaf paths in a binary tree
# time complexity O(n) and space complexity O(h)
# ----------------------------------------------------------------------------

# Binary tree encoding integers

# root is 1
A = BinaryTreeNode(data=1)

# right 1 and left 0 from parent
B = BinaryTreeNode(data=0)
C = BinaryTreeNode(data=0)
D = BinaryTreeNode(data=0)
E = BinaryTreeNode(data=1)
F = BinaryTreeNode(data=1)
G = BinaryTreeNode(data=1)
H = BinaryTreeNode(data=0)
I = BinaryTreeNode(data=1)
J = BinaryTreeNode(data=0)
K = BinaryTreeNode(data=0)
L = BinaryTreeNode(data=1)
M = BinaryTreeNode(data=1)
N = BinaryTreeNode(data=0)
O = BinaryTreeNode(data=0)
P = BinaryTreeNode(data=0)


A.left = B
B.left = C
C.left = D
C.right = E
B.right = F
F.right = G
G.left = H

A.right = I
I.left = J
J.right = K
K.right = N
K.left = L
L.right = M

I.right = O
O.right = P

def sum_root_to_leaf(tree, partial_path_sum=0):

    if not tree:
        return 0

    print(f'partial_path_sum : {partial_path_sum}')
    partial_path_sum = partial_path_sum * 2 + tree.data

    # leaf
    if not tree.left and not tree.right:
        return partial_path_sum

    # non-leaf
    return (sum_root_to_leaf(tree.left, partial_path_sum) +
            sum_root_to_leaf(tree.right, partial_path_sum))


# ----------
# root as A
print(sum_root_to_leaf(A))

# root as L: path from L to leaf: only L --> M
print(sum_root_to_leaf(L))


# ----------------------------------------------------------------------------
# has path sum:
# program takes and input an integer and a binary tree with integer node weights,
# and checks if there exists a leaf whose path weight equals the given integer
# time complexity O(n) and space complexity O(h)
# ----------------------------------------------------------------------------

class BinaryTreeNode:

    def __init__(self, node_name=None, data=None, left=None, right=None):

        self.node = node_name
        self.data = data
        self.left = left
        self.right = right


# ----------
# create root = A
A = BinaryTreeNode(data=314, node_name='A')

# create other nodes
B = BinaryTreeNode(data=6, node_name='B')
C = BinaryTreeNode(data=271, node_name='C')
D = BinaryTreeNode(data=28, node_name='D')
E = BinaryTreeNode(data=0, node_name='E')
F = BinaryTreeNode(data=561, node_name='F')
G = BinaryTreeNode(data=3, node_name='G')
H = BinaryTreeNode(data=17, node_name='H')
I = BinaryTreeNode(data=6, node_name='I')
J = BinaryTreeNode(data=2, node_name='J')
K = BinaryTreeNode(data=1, node_name='K')
L = BinaryTreeNode(data=401, node_name='L')
M = BinaryTreeNode(data=641, node_name='M')
N = BinaryTreeNode(data=257, node_name='N')
O = BinaryTreeNode(data=271, node_name='O')
P = BinaryTreeNode(data=28, node_name='P')


A.left = B
B.left = C
C.left = D
C.right = E
B.right = F
F.right = G
G.left = H

A.right = I
I.left = J
J.right = K
K.right = N
K.left = L
L.right = M

I.right = O
O.right = P

def has_path_sum(tree, remaining_weight):

    if not tree:
        return False

    print(f'node : {tree.node} - data: {tree.data}')

    # leaf
    if not tree.left and not tree.right:
        return remaining_weight == tree.data

    # Non-leaf
    return (has_path_sum(tree.left, remaining_weight - tree.data) or
            has_path_sum(tree.right, remaining_weight - tree.data))



# ----------
# 619: ABCD, AIOP
has_path_sum(A, 619)


# 901: AEGH
has_path_sum(A, 901)


# ----------------------------------------------------------------------------
# Inorder Traversal without recursion
# time complexity O(n) and space complexity O(h)
# ----------------------------------------------------------------------------

def inorder_traversal(tree):

    s, result, result_node = [], [], []

    while s or tree:
        if tree:
            print(f'1: {tree.node}')
            s.append(tree)
            # Going left.
            tree = tree.left
        else:
            # Going up.
            tree = s.pop()
            print(f'  2: inorder traversal: {tree.node}')
            result.append(tree.data)
            result_node.append(tree.node)
            # Going right.
            tree = tree.right

    return result, result_node


# ----------
print(inorder_traversal(A))


# ----------------------------------------------------------------------------
# Preorder Traversal without recursion
# time complexity O(n) and space complexity O(h)
# ----------------------------------------------------------------------------

def preorder_traversal(tree):

    path, result, result_node = [tree], [], []

    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            result_node.append(curr.node)
            path += [curr.right, curr.left]

    return result, result_node


# ----------
print(preorder_traversal(A))


# ----------------------------------------------------------------------------
# Compute the k-th node in an inorder traversal by O(h) time complexity
# ----------------------------------------------------------------------------

# each node stores the number of nodes in the subtree rooted at that node

class BinaryTreeNode:

    def __init__(self, node_name=None, data=None, left=None, right=None, size=None):

        self.node = node_name
        self.data = data
        self.left = left
        self.right = right
        self.size = size


# ----------
# create root = A
A = BinaryTreeNode(data=314, size=15, node_name='A')

# create other nodes
B = BinaryTreeNode(data=6, size=6, node_name='B')
C = BinaryTreeNode(data=271, size=2, node_name='C')
D = BinaryTreeNode(data=28, size=0, node_name='D')
E = BinaryTreeNode(data=0, size=0, node_name='E')
F = BinaryTreeNode(data=561, size=2, node_name='F')
G = BinaryTreeNode(data=3, size=1, node_name='G')
H = BinaryTreeNode(data=17, size=0, node_name='H')
I = BinaryTreeNode(data=6, size=7, node_name='I')
J = BinaryTreeNode(data=2, size=4, node_name='J')
K = BinaryTreeNode(data=1, size=3, node_name='K')
L = BinaryTreeNode(data=401, size=1, node_name='L')
M = BinaryTreeNode(data=641, size=0, node_name='M')
N = BinaryTreeNode(data=257, size=0, node_name='N')
O = BinaryTreeNode(data=271, size=1, node_name='O')
P = BinaryTreeNode(data=28, size=0, node_name='P')


A.left = B
B.left = C
C.left = D
C.right = E
B.right = F
F.right = G
G.left = H

A.right = I
I.left = J
J.right = K
K.right = N
K.left = L
L.right = M

I.right = O
O.right = P


def find_kth_node_binary_tree(tree, k):

    while tree:
        left_size = tree.left.size if tree.left else 0

        # k-th node must be in right subtree of tree
        if left_size + 1 < k:
            k -= left_size + 1
            tree = tree.right

        # k-th is iter itself.
        elif left_size == k - 1:
            return tree

        # k-th node must be in left subtree of iter
        else:
            tree = tree.left

    # If k is between 1 and the tree size, this is unreachable
    return None



# ----------
tree = A
k = 3

# 3rd node in inorder traversal is B
# but it takes O(n)
print(inorder_traversal(tree))

# this takes O(h)
print(find_kth_node_binary_tree(tree, k).node)

