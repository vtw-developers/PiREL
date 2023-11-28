# using assert in tests

###### from chapter_02.linked_list import LinkedList begin ######



class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def values(self):
        return [x.value for x in self]

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(v)




class DoublyLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, None, self.tail)
            self.tail = self.tail.next
        return self

###### from chapter_02.linked_list import LinkedList end ######


def is_palindrome(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True


def is_palindrome_constant_space(ll):
    """
    Constant(O(1)) space solution
    """
    # find the list center via the runner technique
    slow = ll.head
    if not slow or not slow.next:
        return True

    fast = slow.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # unlink left and right halves of the list
    right_head = slow.next
    slow.next_node = None
    # reverse the right half of the list
    tail = reverse(right_head)
    # iterate over nodes from the outside in
    left, right = ll.head, tail
    result = True
    while left and right:
        if left.value != right.value:
            result = False
            break
        left = left.next
        right = right.next
    # undo state changes
    reverse(tail)
    slow.next_node = right_head
    return result


def reverse(node):
    """
    reverses a linked list,
    returns the input list's
    tail node as the new head

        Time : O(N)
        Space: O(1)
    """
    previous_node = None
    while node:
        # keep track of the next node
        next_node = node.next
        # point the current node backwards
        node.next = previous_node
        # advance pointers
        previous_node = node
        node = next_node
    return previous_node


def is_palindrome_recursive(ll):
    def get_len(node):
        if not node:
            return 0
        else:
            return 1 + get_len(node.next)

    def recursive_transverse(node, length):
        if not node or length == 0:  
            return True, node
        elif length == 1:  
            return True, node.next

        _is_palindrome, fwd_node = recursive_transverse(node.next, length - 2)

        if not _is_palindrome or not fwd_node:
            return False, None

        if node.value == fwd_node.value:
            return True, fwd_node.next
        else:
            return False, None

    return recursive_transverse(ll.head, get_len(ll.head))[0]


test_cases = [
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1], True),
    (["a", "a"], True),
    ("aba", True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2], False),
]

testable_functions = [
    is_palindrome,
    is_palindrome_constant_space,
    is_palindrome_recursive,
]


def test_is_palindrome():
    for f in testable_functions:
        for values, expected in test_cases:
            for _ in range(100):
                assert f(LinkedList(values)) == expected



if __name__ == "__main__":
    test_is_palindrome()
