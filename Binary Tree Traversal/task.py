# Pre-order traversal
def pre_order(node):
    if node is None:
        return []  # Indicates end of traversal
    if node.left is None and node.right is None:
        return [node.data]  # Leaf node

    left_subtree = pre_order(node.left)
    right_subtree = pre_order(node.right)

    return [node.data] + left_subtree + right_subtree

# In-order traversal
def in_order(node):
    if node is None:
        return []  # Indicates end of traversal
    if node.left is None and node.right is None:
        return [node.data]  # Leaf node

    left_subtree = in_order(node.left)
    right_subtree = in_order(node.right)

    return left_subtree + [node.data] + right_subtree


# Post-order traversal
def post_order(node):
    if node is None:
        return []  # Indicates end of traversal
    if node.left is None and node.right is None:
        return [node.data]  # Leaf node

    left_subtree = post_order(node.left)
    right_subtree = post_order(node.right)

    return left_subtree + right_subtree + [node.data]
