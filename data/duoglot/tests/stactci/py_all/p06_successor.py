# using assert in tests
###### from chapter_04.binary_search_tree import BinarySearchTree begin ######
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new = Node(key)
        if self.root is None:
            self.root = new
            return

        current = self.root
        while current:
            if current.key > key:
                if current.left is None:
                    current.left = new
                    new.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    new.parent = current
                    return
                current = current.right

    def get_node(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current

            if current.key > key:
                current = current.left
            else:
                current = current.right
        raise Exception("No such value in the tree")


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

###### from chapter_04.binary_search_tree import BinarySearchTree end ######


def in_order_successor(input_node):
    if input_node is None:
        return None

    if input_node.right:
        current = input_node.right
        while current.left:
            current = current.left
        return current

    ancestor = input_node.parent
    child = input_node
    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent
    return ancestor


def test_in_order_successor():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Test all nodes
    inputs = [5, 9, 11, 12, 14, 20, 25]
    outputs = inputs[1:]
    outputs.append(None)

    for x, y in zip(inputs, outputs):
        test = bst.get_node(x)
        succ = in_order_successor(test)
        if succ is not None:
            assert succ.key == y
        else:
            assert succ == y


if __name__ == "__main__":
    test_in_order_successor()
