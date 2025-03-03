# Tree
A bunch of stuff about trees I need to make a routine out of it

## Traversal

At the heart of tree is to traverse a tree to access the nodes. Given it's unique structure, traversal methods are not as straight forward as a for-loop in array.

Recursive traversal methods are straight forward. The problem comes when traversing iteratively 

### Preorder traversal

Preorder means root comes first. Then left, right subtrees.

Recursively, this is trivial. Handle root, handle left, handle right.



## Serialization

To serialize, can choose DFS/BFS. Although preorder stack traversal do serialize it, it does not give the nice parent/child indexing relationship BFS does.

For example, a stack-based serialization will output "54##3##" where 5 is root, left child is 4 with no children and right child is 3 with no children.

BFS will output "543####" which is the level order traversal.

This will be helpful as for ith node, left child index = 2\*i+1 and right child index = 2\*+2

To deserialize, can use recursive
