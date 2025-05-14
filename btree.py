class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._add_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._add_recursive(current_node.right, value)

    def in_order(self, node):
        if node is None:
            return []
        return self.in_order(node.left) + [node.value] + self.in_order(node.right)

    def pre_order(self, node):
        if node is None:
            return []
        return [node.value] + self.pre_order(node.left) + self.pre_order(node.right)

    def post_order(self, node):
        if node is None:
            return []
        return self.post_order(node.left) + self.post_order(node.right) + [node.value]

    def remove(self, value):
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, current_node, value):
        if current_node is None:
            return None

        if value < current_node.value:
            current_node.left = self._remove_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._remove_recursive(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            min_value_node = self._find_min(current_node.right)
            current_node.value = min_value_node.value
            current_node.right = self._remove_recursive(current_node.right, min_value_node.value)

        return current_node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(50)
    tree.add(30)
    tree.add(20)
    tree.add(40)
    tree.add(70)
    tree.add(60)
    tree.add(80)

    print("In-order:", tree.in_order(tree.root))
    print("Pre-order:", tree.pre_order(tree.root))
    print("Post-order:", tree.post_order(tree.root))

    tree.remove(20)
    print("In-order after removing 20:", tree.in_order(tree.root))

    tree.remove(30)
    print("In-order after removing 30:", tree.in_order(tree.root))

    tree.remove(50)
    print("In-order after removing 50:", tree.in_order(tree.root))