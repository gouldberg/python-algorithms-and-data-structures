# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# linked lists
# ----------------------------------------------------------------------------

# each node has two entries, a data field and a next field,
# which points to be next node in the list, with the next field of the last node being null.
class ListNode:

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# search for a key
def search_list(L, key):
    while L and L.data != key:
        L = L.next

    # if key was not present in the list, L will have become null.
    return L


# insert a new node after a specified node
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


# delete the node past this one.
# assume node is not a tail.
def delete_after(node):
    node.next = node.next.next



# ----------
e = ListNode(data=2, next=None)
d = ListNode(data=3, next=e)
c = ListNode(data=5, next=d)
b = ListNode(data=3, next=c)
a = ListNode(data=2, next=b)


print(a.next.data)
print(a.next.next.data)


# ----------
# search for a key
print(search_list(L=c, key=2).data)


# ----------
# insert a new node (f) after a node c
f = ListNode(data=1, next=d)
insert_after(node=c, new_node=f)

print(c.next.data)
print(f.next.data)


# ----------
# delete after c
delete_after(node=c)
print(c.next.data)
print(c.next.next.data)
print(f.next.data)


