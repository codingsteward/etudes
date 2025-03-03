
# Test
You are tasked with implementing a backend for managing a tree structure, where each node has relationships like ancestors, siblings, and children. The tree nodes and the following APIs are pre-defined (no need to implement):

class Node {
  vector<Node> getAncestors();        // Returns all ancestor nodes.
  optional<Node> getParent();         // Returns the parent node if it exists.
  int getLevel();                     // Returns the level of the node in the tree.
  vector<Node> getChildren();         // Returns all child nodes of the node.
  vector<Node> getAllNodes(int level); // Returns all nodes at a given level.
};
Your task is to implement the following backend class:

class Backend {
  vector<Node> getDisplayed(Node node);
  void handleAddSelected(Node node);
  void handleDeleteSelected(Node node);
  vector<Node> getDisplayedWithPoints(Node latest_selected, int max_levels);
};
Requirements
Base Question:
Implement getDisplayed(Node node): Returns all selected nodes, their parent(s), and all siblings of the parent(s).
Implement handleAddSelected(Node node) and handleDeleteSelected(Node node) to manage selected nodes:
handleAddSelected: Marks a node as selected and updates points for the selected node, its ancestors, and its siblings.
handleDeleteSelected: Removes a node from the selected state and adjusts points for the node, its ancestors, and its siblings. Nodes with total points of 0 should no longer appear in the display.
Follow-Up 1:
Refactor the shared logic between handleAddSelected(Node node) and handleDeleteSelected(Node node) into a private API. This API should return the node itself, its parent, and all its siblings, facilitating updates to their points.
Follow-Up 2:
Implement getDisplayedWithPoints(Node latest_selected, int max_levels):
Include the latest_selected node, its ancestors, and siblings in the display.
Assign points to nodes as follows:
Selected node: 3 points
Ancestor of a selected node: 2 points
Sibling of a selected node: 1 point
Limit the display to at most max_levels consecutive levels, ensuring latest_selected is included.
Maximize the total points of displayed nodes within the max_levels constraint.
Additional Details
Level Selection in getDisplayedWithPoints:
The tree may have many levels, but the display can only show max_levels consecutive levels. The API must ensure that the latest_selected node's level is included in the displayed range and the total points are maximized.
Example:
Level 1: Node A (2 points)  
Level 2: Node B (1 point), Node C (3 points)  
Level 3: Node D (0 points)  
If getDisplayedWithPoints(Node B, 2) is called, the result should be {A, B, C}, not {B, C, D}.
Point Updates:
Adding a selected node updates points for:
Selected Node: Gains 3 points.
Ancestors: Each ancestor gains 2 points.
Siblings: Each sibling gains 1 point.
Removing a selected node (handleDeleteSelected) reduces these points accordingly. Nodes with a total point of 0 should not appear in the display.

