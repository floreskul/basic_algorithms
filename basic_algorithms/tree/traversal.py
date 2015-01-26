"""
    Tree traversal algorithms implementation.
    Description: http://en.wikipedia.org/wiki/Tree_traversal
    
    DFS-based traversals: pre-order, in-order, post-order.
"""

def pre_order(root, result=[]):
    if root is None:
        return []
    
    result.append(root.value)
    pre_order(root.left)
    pre_order(root.right)

    return result

def in_order(root, result=[]):
    if root is None:
        return []
    
    in_order(root.left)
    result.append(root.value)
    in_order(root.right)

    return result

def post_order(root, result=[]):
    if root is None:
        return []
    
    post_order(root.left)
    post_order(root.right)
    result.append(root.value)

    return result
