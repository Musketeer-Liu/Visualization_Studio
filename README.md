# Visualization_Studio

## Info
A self-built Data Visualization library based on Python

## Setup
Run binary_tree_implement.py to see the preset results <br />
Change the preset input to see new results

## Modules
1. TreeNode/BT: Construct a Binary Tree <br />
    Construct from Scratch <br />
    Recover from inorder/preorder traversal <br />
    Recover from inorder/postorder traversal <br />
    Construct Root with Max each time

2. TreeNode/BST: Construct a Binary Search Tree <br />
    Build the Root <br />
    Insert a Node <br />
    Remove a Node <br />
    Trim in a Range

3. TreeVisualize: Visualize a Tree in Terminal  <br />
    Get Height of the Tree <br />
    Populate the Tree to a completed Tree <br />
    Plot Node Layer (Node Value with/without Dashes) <br />
    Plot Edges Layer

4. TreeIterator: Iterate TreeNode <br />
    Has Next <br />
    Next Node

5. TreeTraverse: Traverse TreeNode <br />
    Traverse Inorder <br />
    Traverse Preorder <br />
    Traverse Postorder <br />
    Traverse Levelorder <br />
    Traverse ZigZagorder <br />
    Traverse Verticalorder <br />
    Tree Paths Collections <br />
    Tree Leaves Collections

6. TreeValid: Validate Properties of a Tree/Relations between two Trees <br />
    Is it a symmetric tree?  <br />
    Is it a completed tree?  <br />
    Is it a valid Binary Search Tree?  <br />
    Are two trees identical? <br />
    Are two trees tweaked identical? <br />  

7. TreeAttribute: Get Basic Values of the Tree <br />
    Node Count of the Tree <br />
    Max Depth of the Tree <br />
    Min Depth of the Tree <br />
    Paths Sum of the Tree <br />
    Leaf Sum of the Tree <br />
    Level Sum of the Tree <br />
    Longest Continue Path from Root to Leaf <br />
    Longest Continue Path freom Anynode to Anynode <br />
    Min Path Sum from Root to Leaf <br />
    Max Path Sum from Anynode to Anynode <br />
    Max Path Sum Downward from Root

8. TreeSearch: Search Node/Value in the Tree <br />
    Max Value in the Tree <br />
    Leaf Node Value cloest to Target <br />
    Max Sum Subtree Root Value <br />
    Min Sum Subtree Root Value <br />
    Max Avg Subtree Root Value <br />
    Min Avg Subtree Root Value <br />
    BST Lowest Common Ancestor Node Value <br />
    BST Lowest Common Ancestor Node Value <br />
    Search Target Paths from Root toLeaf <br />
    Search Target Paths Downward from Root <br />
    Search Target Paths from Anynode to Anynode

9. TreeOperate: Operations on Tree: <br />
    Serialization/Deserialization <br />
    Upsidedown the Tree <br />
    Flatten to Faked Linked List <br />
    Convert to Doubly Linked List <br />


## Future
1. Optimize the README and Library structure according to profession
2. Separate existing big single files into reasonable length modules
3. Optimize TreeNode, BT, BST init values for multiple functions
4. Add more features like connecting parent node automatically
5. Implement visualization on more data structure such as Trie


## Paradigm
Welcome to Smart Tree Library:


BT Initiating  ==>>  BT Constructed!  <br />
You may compared the BT recovered from different order list -- Shoud be the same: <br />
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
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19 <br />
Build with Inorder and Postorder:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19 <br />
Build each root with max value:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19


BST Initiating ==>> BST Constructed! <br />
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
 1~>2~>3~>4~>5~>7~>8~>10~>11~>13~>15~>17~>19~>20~>21 <br />
Iteration after Remove:
 1~>2~>3~>4~>5~>7~>8~>10~>11~>13~>15~>17~>19~>20 <br />
Iteration after Trim:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19 <br /> 
Visualize BST Structure after delete and trim operation:

           ____10____
          /             \
       __5__             15
      /     \         /     \
     4       7      11      17
              \       \       \
               8      13      19




Tree Validation: <br />
Is it a symmetric tree?          False <br />
Is it a completed tree?          False <br />
Is it a valid BST?               True <br />
Is it a valid BST?               True <br />
Are two trees identical?         True <br />
Are two trees tweaked?           True <br />


BST Basic Values: <br />
Node Count of the Tree:          10 <br />
Max Depth of the Tree:           4 <br />
Min Depth of the Tree:           3 <br />
Paths Sum of the Tree:           34944 <br />
Leaf Sum of the Tree:            44 <br />
Level Sum of the Tree:           39 <br />
Longest Continue Path RootLeaf:  2 <br />
Longest Continue Path Anywhere:  2 <br />
Min Path Sum RootLeaf:           19 <br />
Max Path Sum Anywhere:           81 <br />
Max Path Sum FromRoot:           61


Traversal of BST: <br />
Traverse Inorder:
 [4, 5, 7, 8, 10, 11, 13, 15, 17, 19] <br />
Traverse Preorder:
 [10, 5, 4, 7, 8, 15, 11, 13, 17, 19] <br />
Traverse Postorder:
 [4, 8, 7, 5, 13, 11, 19, 17, 15, 10] <br />
Traverse Levelorder:
 [[10], [5, 15], [4, 7, 11, 17], [8, 13, 19]] <br />
Traverse ZigZagorder:
 [[10], [15, 5], [4, 7, 11, 17], [19, 13, 8]] <br />
Traverse Verticalorder:
 [[4], [5], [10, 7, 11], [15, 8, 13], [17], [19]] <br />
Tree Paths Collections:
 ['10->5->4', '10->5->7->8', '10->15->11->13', '10->15->17->19'] <br />
Tree Leaves Collections:
 [[4, 8, 13, 19], [7, 11, 17], [5, 15], [10]]


Search in BST: <br />
Max Value in the Tree:           19 <br />
Leaf Value cloest to Target:     4 <br />
Max Sum Subtree Root Value:      10 <br />
Min Sum Subtree Root Value:      4 <br />
Max Avg Subtree Root Value:      19 <br />
Min Avg Subtree Root Value:      4 <br />
BST Lowest Common Ancestor:      5 <br />
BST Lowest Common Ancestor:      None <br />
Search Target Paths RootLeaf:
 [[10, 5, 4]] <br />
Search Target Paths Downward:
 [[10, 5, 4], [19]] <br />
Search Target Paths Anywhere:
 [[10, 5, 4], [19]]


Operation on BST:

Serialization and Deserialization: <br />
String from Tree Serialization:
 10,5,15,4,7,11,17,#,#,#,8,#,13,#,19,#,#,#,#,#,#, <br />
Iteration from Deserializaion:
 4~>5~>7~>8~>10~>11~>13~>15~>17~>19


Convert to other Data Structure: <br />
Convert to Fake Linked List:
 10->5->4->7->8->15->11->13->17->19 <br />
Convert to Doubly Linked List:
 10<=>5<=>4<=>7<=>8<=>15<=>11<=>13<=>17<=>19


Upsidedown the Tree: <br />
BST Initiating ==>> BST Constructed! <br />
Traverse before Upsidwon:
 [[10], [5, 15], [4, 7, 11, 17], [8, 13, 19]] <br />
Visualize BST Structure in original construction:

           ____10____
          /             \
       __5__             15
      /     \         /     \
     4       7      11      17
              \       \       \
               8      13      19

Traverse after Iteration Upsidown:
 [[4], [7, 5], [8, 15, 10], [11, 17], [13, 19]] <br />
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

BST Initiating ==>> BST Constructed! <br />
Traverse before Upsidwon:
 [[10], [5, 15], [4, 7, 11, 17], [8, 13, 19]] <br />
Visualize BST Structure in original construction:

           ____10____
          /             \
       __5__             15
      /     \         /     \
     4       7      11      17
              \       \       \
               8      13      19

Traverse after Recursion Upsidown:
 [[4], [7, 5], [8, 15, 10], [11, 17], [13, 19]] <br />
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