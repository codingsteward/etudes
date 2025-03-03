# Tree traversals
from typing import Optional
from collections.abc import Sequence
from collections import deque

class TreeNode:
    def __init__(self, item=0, left:Optional['TreeNode']=None, right:Optional['TreeNode']=None) -> 'TreeNode':
        self.item = item
        self.left = left
        self.right = right

def serialize_tree(root: Optional[TreeNode]) -> str:
    """Serialise tree in preorder traversal and convert
    into a array"""
    def helper(node: Optional[TreeNode], xs: list) -> str:
        if node is None:
            xs.append('#')
        else:
            xs.append(str(node.item))
            helper(node.left, xs)
            helper(node.right, xs)

    xs = []
    helper(root, xs)
    return ','.join(xs)

def deserialize_tree(s: str) -> Optional[TreeNode]:
    """Deserialize a tree which was stored in preorder way
    """
    def helper():
        item = next(data)
        if item == "#":
            return None
        root = TreeNode(int(item))
        root.left = helper()
        root.right = helper()
        return root
    
    data = iter(s.split(','))
    return helper()

def serialize_iter(root: Optional[TreeNode]) -> str:
    """Serialize a tree iteratively using level order traversal with queue"""
    q, res = deque([root]), []
    while q:
        node = q.popleft()
        if node:
            res.append(str(node.item))
            q.append(node.left)
            q.append(node.right)
        else:
            res.append('#')
    return ",".join(res)

def deserialize_iter(data: str) -> Optional[TreeNode]:
    if data[0] == '#':
        return
    vals = iter(data.split(','))
    root = TreeNode(int(next(vals)))
    q = deque([root])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            left, right = next(vals), next(vals)
            if left != '#':
                node.left = TreeNode(int(left))
                q.append(node.left)
            if right != '#':
                node.right = TreeNode(int(right))
                q.append(node.right)
    return root

a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(3)
a.left = b
a.right = c


def is_equal(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    if s is None and t is None: return True
    if s is None or t is None: 
        return False
    return s.item == t.item and is_equal(s.left, t.left) and is_equal(s.right, t.right)

print("serialize iter", s := serialize_iter(a))
print("deserialize iter", t := deserialize_iter(s))
print("is equal", is_equal(a, t))

def print_tree(root: Optional[TreeNode]) -> str:
    if not root:
        return '_'
    return str(root.item) + ' ' + print_tree(root.left) + ' ' + print_tree(root.right)

print(print_tree(t))
print(print_tree(a))

a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(3)
a.left = b
a.right = c

s = serialize_tree(a)
print("serialize recursive", s)
tree = deserialize_tree(s)

print(is_equal(tree, a))

node = TreeNode(5)
node = TreeNode(3)
print(node.item)

