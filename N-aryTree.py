class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def encode(root: 'Node') -> 'TreeNode':
    if not root:
        return None
    
    binary_root = TreeNode(root.val)
    if root.children:
        binary_root.left = encode(root.children[0])
        
    current = binary_root.left
    for child in root.children[1:]:
        current.right = encode(child)
        current = current.right
        
    return binary_root

def decode(root: 'TreeNode') -> 'Node':
    if not root:
        return None
    
    nary_root = Node(root.val)
    current = root.left
    while current:
        nary_root.children.append(decode(current))
        current = current.right
        
    return nary_root

# Example usage:
# Building an N-ary tree
nary_root = Node(1, [
    Node(2),
    Node(3),
    Node(4, [Node(5), Node(6)])
])

# Encoding the N-ary tree to a binary tree
binary_root = encode(nary_root)

# Decoding the binary tree back to an N-ary tree
decoded_nary_root = decode(binary_root)

def print_nary_tree(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        queue.extend(node.children)
        if not queue:
            result.append(-1)
    return result

# Printing the original and decoded N-ary trees
print("Original N-ary tree:", print_nary_tree(nary_root))
print("Decoded N-ary tree:", print_nary_tree(decoded_nary_root))
