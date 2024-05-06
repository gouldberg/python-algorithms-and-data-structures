# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Binary Trees
# ----------------------------------------------------------------------------

class BinaryTreeNode:

    def __init__(self, node_name=None, data=None, left=None, right=None):

        self.node = node_name
        self.data = data
        self.left = left
        self.right = right


# ----------
# create root = A
A = BinaryTreeNode(node_name='A', data=314)

# create other nodes
B = BinaryTreeNode(node_name='B', data=6)
C = BinaryTreeNode(node_name='C', data=271)
D = BinaryTreeNode(node_name='D', data=28)
E = BinaryTreeNode(node_name='E', data=0)
F = BinaryTreeNode(node_name='F', data=561)
G = BinaryTreeNode(node_name='G', data=3)
H = BinaryTreeNode(node_name='H', data=17)
I = BinaryTreeNode(node_name='I', data=6)
J = BinaryTreeNode(node_name='J', data=2)
K = BinaryTreeNode(node_name='K', data=1)
L = BinaryTreeNode(node_name='L', data=401)
M = BinaryTreeNode(node_name='M', data=641)
N = BinaryTreeNode(node_name='N', data=257)
O = BinaryTreeNode(node_name='O', data=271)
P = BinaryTreeNode(node_name='P', data=28)


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
# lowest common ancestor (LCA) in a binary tree
# time complexity: O(n) and space complexity O(h)
# ----------------------------------------------------------------------------

import collections

def lca(tree, node0, node1):

    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    # Returns an object consisting of an int and a node.
    # The int field is 0, 1, or 2 depending on how many of {node0, node1} are present in tree.
    # If both are present in tree, when ancestor is assigned to a non-null value, it is the LCA.

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)

        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result

        right_result = lca_helper(tree.right, node0, node1)

        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree.
            return right_result

        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes +
                            (node0, node1).count(tree))

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor



# ----------
t = lca(tree=A, node0=L, node1=P)

t.node

t.data


# ----------------------------------------------------------------------------
# lowest common ancestor (LCA) in a binary tree
# time complexity: O(h) and space complexity O(1)
# ----------------------------------------------------------------------------

# here each node has parent pointer
class BinaryTreeNode2:

    def __init__(self, node_name=None, data=None, parent=None):

        self.node = node_name
        self.data = data
        self.parent = parent


# ----------
# create root = A
A = BinaryTreeNode2(node_name='A', data=314)

# create other nodes
B = BinaryTreeNode2(node_name='B', data=6, parent=A)
C = BinaryTreeNode2(node_name='C', data=271, parent=B)
D = BinaryTreeNode2(node_name='D', data=28, parent=C)
E = BinaryTreeNode2(node_name='E', data=0, parent=C)
F = BinaryTreeNode2(node_name='F', data=561, parent=B)
G = BinaryTreeNode2(node_name='G', data=3, parent=F)
H = BinaryTreeNode2(node_name='H', data=17, parent=G)
I = BinaryTreeNode2(node_name='I', data=6, parent=A)
J = BinaryTreeNode2(node_name='J', data=2, parent=I)
K = BinaryTreeNode2(node_name='K', data=1, parent=J)
L = BinaryTreeNode2(node_name='L', data=401, parent=K)
M = BinaryTreeNode2(node_name='M', data=641, parent=L)
N = BinaryTreeNode2(node_name='N', data=257, parent=K)
O = BinaryTreeNode2(node_name='O', data=271, parent=I)
P = BinaryTreeNode2(node_name='P', data=28, parent=O)


# ----------
def lca2(node0, node1):

    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))

    # Makes node0 as the deeper node in order to simplify the code.
    if depth1 < depth0:
        node0, node1 = node1, node0

    # Ascends from the deeper node.
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1


    # Now ascends both nodes until we reach the LCA.
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent

    return node0


# ----------
t = lca2(node0=L, node1=P)

t.node
