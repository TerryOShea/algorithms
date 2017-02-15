def valid_bs_tree(root):
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()
        if (node.value < lower_bound) or (node.value > upper_bound):
            return False
        if node.left:
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    return True

def valid_bst(root, lower_bound = -float('inf'), upper_bound = float('inf')):
    if not root: return True
    if root.value < lower_bound or root.value > upper_bound: return False
    return valid_bst(root.left, lower_bound, root.value) and \
           valid_bst(root.right, root.value, upper_bound)
