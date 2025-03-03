# Implement backend API for node
from typing import Optional

class Node:
    def __init__(self, item=None, parent=None, children=[], level=None):
        self.item = item
        self.parent = parent
        self.children = children
        self.level = level

    def getAncestors(self) -> list['Node']:
        curr = self
        ancestors = []
        while curr.parent:
            curr = curr.parent
            ancestors.append(curr)
        return ancestors

    def getParent(self) -> Optional['Node']:
        return self.parent

    def getLevel(self) -> int:
        return self.level

    def getChildren(self) -> list['Node']:
        return self.children

    def getAllNodes(self, level: int) -> list['Node']:
        curr = self
        while curr.parent:
            curr = curr.parent
        # level order BFS
        q = [curr]
        curr_level = 1
        while q:
            new_q = []
            curr_level += 1
            for node in q:
                for child in node.children:
                    new_q.append(child)
            if curr_level == level:
                return new_q
            else:
                q = new_q


        pass

    def __str__(self) -> str:
        def helper(node, level):
            # each node is printed on a new line
            # each node is prefixed with indentation x level
            res = "  " * 2 * level + str(node.item)
            for child in node.children:
                res += "\n" + helper(child, level+1)
            return res

        return helper(self, 0)

root = Node(-1, level=1)
parents = []
for i in range(3):
    parent = Node(i, root, level=2)
    parents.append(parent)
    children = []
    for j in range(3):
        children.append(Node(i*3+j+3, parent, level=3))
    parent.children = children
root.children = parents

print(root.getAllNodes(3))
for node in root.getAllNodes(2):
    print(node)

# define additional helper class to set up n-ary tree

# each node only has one parent, but a parent might have multiple nodes


class Backend:

    def getDisplayed(self, node: Node) -> list[Node]:
        "Returns all selected nodes, their parents, siblings of parents"

        selected_nodes = []
        for selected in selected_nodes:
            parent = selected.getParent()
            # a parent sibling is the parent's parent's children
            siblings = parent.getParent().children() if parent else []
        pass

    def handleAddSelected(self, node: Node) -> None:
        pass

    def handleDeleteSelected(self, node: Node) -> None:
        pass

    def getDisplayedWIthPoints(self, latest_selected: Node, max_levels: int) -> list[Node]:
        pass

db = Backend()

db.getDisplayed()




