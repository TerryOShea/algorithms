# superbalanced: the difference between the depths of any two leaf
# nodes is no more than 1
def is_superbalanced(binary_tree_root):
    leaf_depths = []
    nodes = [(binary_tree_root, 0)]

    while len(nodes):
        node, depth = node.pop()
        if not node.left and not node.right:
            if depth not in leaf_depths:
                leaf_depths.append(depth)
                if len(leaf_depths) > 2 or abs(leaf_depths[0] - leaf_depths[1]) > 1:
                    return False
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True
