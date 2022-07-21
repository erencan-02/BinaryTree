from enum import Enum


class Comparator:
    def compare(self, a, b) -> int:
        pass


class IntComparator(Comparator):
    def compare(self, a, b):
        return 1 if a > b else (0 if a == b else -1)


class TraversalOrder(Enum):
    IN_ORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, nodes, comparator):

        self.root = None if len(nodes) == 0 else Node(nodes[0])
        self.comparator = comparator
        self.createTree([Node(i) for i in nodes[1:]])

    def createTree(self, nodes):
        for n in nodes:
            self.insert(n)

    def convertToNode(self, value):
        if isinstance(value, Node):
            return value

        return Node(value)

    def insertCollection(self, nodes: list) -> bool:
        for n in [self.convertToNode(i) for i in nodes]:
            self.insert(n)

    def insert(self, node) -> bool:
        node = self.convertToNode(node)

        if self.root is None:
            self.root = node
            return True

        p = self.root

        while True:
            if self.comparator.compare(node.key, p.key) == -1:
                if p.left is None:
                    p.left = node
                    return True
                p = p.left
            else:
                if p.right is None:
                    p.right = node
                    return True
                p = p.right

    @staticmethod
    def traverse(root, order=TraversalOrder.IN_ORDER):
        lst = []
        BinaryTree.traverseHelper(root, order, lst)
        return lst

    @staticmethod
    def traverseHelper(root, order, lst):
        if root is None:
            return

        if order is TraversalOrder.PRE_ORDER:
            lst.append(root.key)

        BinaryTree.traverseHelper(root.left, order, lst)

        if order is TraversalOrder.IN_ORDER:
            lst.append(root.key)

        BinaryTree.traverseHelper(root.right, order, lst)

        if order is TraversalOrder.POST_ORDER:
            lst.append(root.key)


tree = BinaryTree((10, 9, 15, 12, 25, -1, -100, -101), IntComparator())

print(tree.traverse(tree.root, order=TraversalOrder.IN_ORDER))
