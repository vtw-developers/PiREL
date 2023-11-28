###### from chapter_04.binary_tree import BinaryTree begin ######
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    NodeCls = Node

    def __init__(self):
        self.root = None

    def insert(self, key, parent):
        new = self.NodeCls(key)
        if parent is None:
            if self.root is None:
                self.root = new
                return new
            raise Exception("a root already exists")

        if not parent.left:
            parent.left = new
            new.parent = parent
        elif not parent.right:
            parent.right = new
            new.parent = parent
        else:
            raise Exception("a node cannot have more than two children")
        return new


def example():
    t = BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    t.insert(5, n2)
    t.insert(7, n3)
    t.insert(8, n4)

    print(t.root.left.left.left.key)


if __name__ == "__main__":
    example()

###### from chapter_04.binary_tree import BinaryTree end ######, Node


class ComparableTreeNode(Node):
    def __eq__(self, other):
        if not isinstance(other, ComparableTreeNode):
            return False
        return (
            self.key == other.key
            and self.left == other.left
            and self.right == other.right
        )


class ComparableBinaryTree(BinaryTree):
    NodeCls = ComparableTreeNode


# "needle in a haystack"
# haystack == the thing we're searching inside
# needle == the thing we're looking for
def is_subtree(haystack_tree, needle_tree):
    if not haystack_tree or not needle_tree:
        return False
    return _is_subtree(haystack_tree.root, needle_tree.root)


def _is_subtree(haystack_node, needle_node):
    if haystack_node is None or needle_node is None:
        return False
    if haystack_node == needle_node:
        return True

    return _is_subtree(haystack_node.left, needle_node) or _is_subtree(
        haystack_node.right, needle_node
    )


if __name__ == "__main__":
    t1 = ComparableBinaryTree()
    n1 = t1.insert(1, None)
    n2 = t1.insert(2, n1)
    n3 = t1.insert(3, n1)
    n4 = t1.insert(4, n2)
    n5 = t1.insert(5, n2)
    n7 = t1.insert(7, n3)
    n8 = t1.insert(8, n4)

    t2 = ComparableBinaryTree()
    n40 = t2.insert(4, None)
    n80 = t2.insert(8, n40)
    # n90 = t2.insert(9, n40)

    print(is_subtree(t1, t2))
