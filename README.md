# Visualization_Studio

## Info
A self-built Data Visualization library based on Python

## Setup
Run binary_tree_implement.py to see the preset results
Change the preset input to see new results

## Modules
1. TreeNode/BT: Construct a Binary Tree 
    Construct from Scratch
    Recover from inorder/preorder traversal
    Recover from inorder/postorder traversal
    Construct Root with Max each time

2. TreeNode/BST: Construct a Binary Search Tree 
    Build the Root
    Insert a Node
    Remove a Node
    Trim in a Range

3. TreeVisualize: Visualize a Tree in Terminal:
    Get Height of the Tree
    Populate the Tree to a completed Tree
    Plot Node Layer (Node Value with/without Dashes)
    Plot Edges Layer

4. TreeIterator: Iterate TreeNode one by one with has_next() and next_node()
    Has Next
    Next Node

5. TreeTraverse: Traverse TreeNode of the Tree:
    Traverse Inorder
    Traverse Preorder
    Traverse Postorder
    Traverse Levelorder
    Traverse ZigZagorder
    Traverse Verticalorder
    Tree Paths Collections
    Tree Leaves Collections

6. TreeValid: Validate Properties of a Tree/Relations between two Trees:
    Is it a symmetric tree? 
    Is it a completed tree? 
    Is it a valid Binary Search Tree? 
    Are two trees identical? 
    Are two trees tweaked identical?  

7. TreeAttribute: Get Basic Values of the Tree:
    Node Count of the Tree
    Max Depth of the Tree
    Min Depth of the Tree
    Paths Sum of the Tree
    Leaf Sum of the Tree
    Level Sum of the Tree
    Longest Continue Path from Root to Leaf
    Longest Continue Path freom Anynode to Anynode
    Min Path Sum from Root to Leaf
    Max Path Sum from Anynode to Anynode
    Max Path Sum Downward from Root

8. TreeSearch: Search Node/Value in the Tree:
    Max Value in the Tree
    Leaf Node Value cloest to Target
    Max Sum Subtree Root Value
    Min Sum Subtree Root Value
    Max Avg Subtree Root Value
    Min Avg Subtree Root Value
    BST Lowest Common Ancestor Node Value
    BST Lowest Common Ancestor Node Value
    Search Target Paths from Root toLeaf
    Search Target Paths Downward from Root
    Search Target Paths from Anynode to Anynode

9. TreeOperate: Operations on Tree:
    Serialization/Deserialization
    Upsidedown the Tree
    Flatten to Faked Linked List
    Convert to Doubly Linked List


## Future
1. Optimize the README and Library structure according to profession
2. Separate existing big single files into reasonable length modules
3. Optimize TreeNode, BT, BST init values for multiple functions
4. Add more features like connecting parent node automatically
5. Implement visualization on more data structure such as Trie


## Paradigm
Welcome to Smart Tree Library:


BT Initiating  ==>>  BT Constructed!
You may compared the BT recovered from different order list -- Shoud be the same:
Visualize BT Structure Recover from Inorder and Preorder:

           ____10____
          /             \
       __5__           15
      /     \         /     \
     4       7      11      17
              \       \       \
               8      13      19

Visualize BT Structure Recover from Inorder and Posorder:

           ____10____
          /             \
       __5__           15
      /     \         /     \
     4       7      11      17
              \       \       \
               8      13      19

Build with Inorder and Preorder:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19
Build with Inorder and Postorder:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19
Build each root with max value:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19


BST Initiating ==>> BST Constructed!
Visualize BST Structure in original construction:

                                   ____________________________10____________________________
                                  /                                                           \
                   ______________5______________                                   ____________15____________
                  /                             \                                 /                            \
           ______4                               7______                       11____                           17____
          /                                             \                             \                                \
         1__                                             8                             13                               20
            \                                                                                                         /     \
             2                                                                                                      19      21
              \
               3

Normal Iteration:
 1~>2~>3~>4~>5~>7~>8~>10~>11~>13~>15~>17~>19~>20~>21
Iteration after Remove:
 1~>2~>3~>4~>5~>7~>8~>10~>11~>13~>15~>17~>19~>20
Iteration after Trim:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19
Visualize BST Structure after delete and trim operation:

           ____10____
          /             \
       __5__             15
      /     \         /     \
     4       7      11      17
              \       \       \
               8      13      19




Tree Validation:
Is it a symmetric tree?          False
Is it a completed tree?          False
Is it a valid BST?               True
Is it a valid BST?               True
Are two trees identical?         True
Are two trees tweaked?           True


BST Basic Values:
Node Count of the Tree:          10
Max Depth of the Tree:           4
Min Depth of the Tree:           3
Paths Sum of the Tree:           34944
Leaf Sum of the Tree:            44
Level Sum of the Tree:           39
Longest Continue Path RootLeaf:  2
Longest Continue Path Anywhere:  2
Min Path Sum RootLeaf:           19
Max Path Sum Anywhere:           81
Max Path Sum FromRoot:           61


Traversal of BST:
Traverse Inorder:
 [4, 5, 7, 8, 10, 11, 13, 15, 17, 19]
Traverse Preorder:
 [10, 5, 4, 7, 8, 15, 11, 13, 17, 19]
Traverse Postorder:
 [4, 8, 7, 5, 13, 11, 19, 17, 15, 10]
Traverse Levelorder:
 [[10], [5, 15], [4, 7, 11, 17], [8, 13, 19]]
Traverse ZigZagorder:
 [[10], [15, 5], [4, 7, 11, 17], [19, 13, 8]]
Traverse Verticalorder:
 [[4], [5], [10, 7, 11], [15, 8, 13], [17], [19]]
Tree Paths Collections:
 ['10->5->4', '10->5->7->8', '10->15->11->13', '10->15->17->19']
Tree Leaves Collections:
 [[4, 8, 13, 19], [7, 11, 17], [5, 15], [10]]


Search in BST:
Max Value in the Tree:           19
Leaf Value cloest to Target:     4
Max Sum Subtree Root Value:      10
Min Sum Subtree Root Value:      4
Max Avg Subtree Root Value:      19
Min Avg Subtree Root Value:      4
BST Lowest Common Ancestor:      5
BST Lowest Common Ancestor:      None
Search Target Paths RootLeaf:
 [[10, 5, 4]]
Search Target Paths Downward:
 [[10, 5, 4], [19]]
Search Target Paths Anywhere:
 [[10, 5, 4], [19]]



Operation on BST:
Serialization and Deserialization:
String from Tree Serialization:
 10,5,15,4,7,11,17,#,#,#,8,#,13,#,19,#,#,#,#,#,#,
Iteration from Deserializaion:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19


Convert to other Data Structure:
Convert to Fake Linked List:
 10->5->4->7->8->15->11->13->17->19
Convert to Doubly Linked List:
 10<=>5<=>4<=>7<=>8<=>15<=>11<=>13<=>17<=>19


Upsidedown the Tree:
BST Initiating ==>> BST Constructed!
Traverse before Upsidwon:
 [[10], [5, 15], [4, 7, 11, 17], [8, 13, 19]]
Visualize BST Structure in original construction:

           ____10____
          /             \
       __5__             15
      /     \         /     \
     4       7      11      17
              \       \       \
               8      13      19

Traverse after Iteration Upsidown:
 [[4], [7, 5], [8, 15, 10], [11, 17], [13, 19]]
Visualize BST Structure after Iteration Upsidown:

                   ______________4______________
                  /                             \
                 7______                   ______5______
                        \                 /             \
                         8               15             10
                                      /     \
                                    11      17
                                      \       \
                                      13      19

BST Initiating ==>> BST Constructed!
Traverse before Upsidwon:
 [[10], [5, 15], [4, 7, 11, 17], [8, 13, 19]]
Visualize BST Structure in original construction:

           ____10____
          /             \
       __5__             15
      /     \         /     \
     4       7      11      17
              \       \       \
               8      13      19

Traverse after Recursion Upsidown:
 [[4], [7, 5], [8, 15, 10], [11, 17], [13, 19]]
Visualize BST Structure after Recursion Upsidown:

                   ______________4______________
                  /                             \
                 7______                   ______5______
                        \                 /             \
                         8               15             10
                                      /     \
                                    11      17
                                      \       \
                                      13      19