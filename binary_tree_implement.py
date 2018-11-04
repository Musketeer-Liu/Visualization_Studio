__author__ = 'Yutong Liu'



from collections import defaultdict, deque
from copy import deepcopy as deepcopy




class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None, children=[]):
        self.val = val 
        self.left, self.right = left, right
        self.parent = parent
        self.children = children

    # def __repr__(self):
    #     return str(self.val)




class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val, self.next, self.prev = val, next, prev

    # def __repr__(self):
    #     return str(self.val)




class BT:
    def __init__(self, root=None, rank=[], range=[float('inf'), float('-inf')],
                 inorder=[], preorder=[], postorder=[], levelorder=[]):
        self.root, self.rank, self.range = root, rank, range
        self.inorder, self.preorder,self.postorder, self.levelorder = inorder, preorder, postorder, levelorder


    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def build_inorder_preorder(self, inorder, preorder):
        if not inorder: return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.build_inorder_preorder(inorder[:idx],preorder[1:idx+1])
        root.right = self.build_inorder_preorder(inorder[idx+1:], preorder[idx+1:])
        return root

    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def build_inorder_postorder(self, inorder, postorder):
        if not inorder: return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.build_inorder_postorder(inorder[:idx], postorder[:idx])
        root.right = self.build_inorder_postorder(inorder[idx+1:], postorder[idx:-1])
        return root

    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def build_maxorder(self, rank):
        stack = []
        for i in rank:
            node = TreeNode(i)
            while stack and i > stack[-1].val:
                node.left = stack.pop()
            if stack: stack[-1].right = node
            stack.append(node)
        return stack[0]




class BST:
    def __init__(self, root=None, rank=[], range=[float('inf'), float('-inf')],
                 inorder=[], preorder=[], postorder=[], levelorder=[]):
        self.root, self.rank, self.range = root, [], range
        self.inorder, self.preorder,self.postorder, self.levelorder = inorder, preorder, postorder, levelorder

    
    def build(self, val):
        if self.root is None: self.root = TreeNode(val)
        else: self._insert(self.root, val)

    def _insert(self, node, value):
        if value < node.val:
            if node.left: self._insert(node.left, value)
            else: node.left = TreeNode(value)
        else:
            if node.right: self._insert(node.right, value)
            else: node.right = TreeNode(value)
    

    # def swap(self, root, v1, v2):
    #     record = self.inorder(root)
    #     if v1 not in record or v2 not in record: return root
    #     i1, i2 = record.index(v1), record.index(v2)
    #     record[i1], record[i2] = v2, v1
    #     bst_swap = BST()
    #     for v in record: bst_swap.build(v)
    #     return bst_swap.root


    def trim(self, root, range):
        if not root: return root
        if root.val < range[0]: return self.trim(root.right, range)
        if root.val > range[1]: return self.trim(root.left, range)
        root.left = self.trim(root.left, range)
        root.right = self.trim(root.right, range)
        return root


    def remove(self, root, value):
        self._order(root, value)
        root_after_remove = self._rebuild(0, len(self.rank)-1)
        return root_after_remove

    def _order(self, node, value):
        if not node: return
        
        self._order(node.left, value)
        if node.val != value: 
            self.rank.append(node.val)
        self._order(node.right, value)

    def _rebuild(self, l, r):
        if l == r: return TreeNode(self.rank[l])
        if l > r: return None
        
        m = (l + r) // 2
        node = TreeNode(self.rank[m])
        node.left = self._rebuild(l, m-1)
        node.right = self._rebuild(m+1, r)
        return node

    





class TreeIterator:
    """
    @param root: The root of binary tree
    """
    def __init__(self, root):
        self.curt, self.stack = root, []

    """
    @return: A boolean on if has next node
    """
    def has_next(self):
        return self.curt or self.stack

    """
    @return: Next Node
    """
    # Inorder Traverse
    def next_node(self):
        while self.curt:
            self.stack.append(self.curt)
            self.curt = self.curt.left
        
        self.curt = self.stack.pop()
        result = self.curt
        self.curt = self.curt.right
        return result








class TreeAttribute:
    """
    @param root: The root of binary tree.
    @return: An integer denotes as node count of the tree.
    """
    def tree_node_count(self, root):
        count = 0
        if root.left: count += self.tree_node_count(root.left)
        if root.right: count += self.tree_node_count(root.right)
        return count+1 


    """
    @param root: The root of binary tree.
    @return: An integer denotes as max depth of the tree.
    """
    # Max Depth of Tree <=> Height of Tree
    def tree_max_depth(self, root):
        if not root: return 0
        l = self.tree_max_depth(root.left)
        r = self.tree_max_depth(root.right)
        return max(l, r) + 1


    """
    @param root: The root of binary tree.
    @return: An integer denotes as min depth of the tree.
    """
    def tree_min_depth(self, root):
        if not root: return 0
        l = self.tree_min_depth(root.left)
        r = self.tree_min_depth(root.right)

        if l == 0 and r == 0: return 1
        elif l == 0 or r == 0: return max(l, r) + 1
        else: return min(l, r) + 1


    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def tree_paths_sum(self, root):
        return self._dfs_paths_sum(root, 0)
    
    def _dfs_paths_sum(self, root, number):
        if not root: return 0

        number = number * 10 + root.val
        if not root.left and not root.right: return number

        lnumber = self._dfs_paths_sum(root.left, number)
        rnumber = self._dfs_paths_sum(root.right, number)
        
        return lnumber+rnumber

    
    """
    @param root: the root of the binary tree
    @return: An integer of the sum of leaves
    """
    def tree_leaf_sum(self, root):
        leaves = []
        self._dfs_leaf_sum(root, leaves)
        return sum(leaves)

    def _dfs_leaf_sum(self, node, leaves):
        if not node: return
        if not node.left and not node.right: 
            return leaves.append(node.val)
        
        self._dfs_leaf_sum(node.left, leaves)
        self._dfs_leaf_sum(node.right, leaves)

    
    """
    @param root: the root of the binary tree
    @param depth: the depth of the target level
    @return: An integer
    """
    def tree_level_sum(self, root, depth):
        level = []
        self._dfs_level_sum(root, 1, depth, level)
        return sum(level)

    def _dfs_level_sum(self, node, index, depth, level):
        if not node: return
        if index == depth:
            return level.append(node.val)
        
        self._dfs_level_sum(node.left, index+1, depth, level)
        self._dfs_level_sum(node.right, index+1, depth, level)


    """
    @param root: The root of a Binary Tree
    @return: A Integer denotes as minimum sum
    Path means from root to leaf node
    """
    # # Normal Approach with Recursion
    # def tree_minpathsum_rootleaf(self, root):
    #     if not root.left and not root.right:
    #         return root.val
    #     if not root.left: 
    #         return root.val + self.tree_minpathsum_rootleaf(root.right)
    #     if not root.right:
    #         return root.val + self.tree_minpathsum_rootleaf(root.left)
        
    #     l, r = self.tree_minpathsum_rootleaf(root.left), self.tree_minpathsum_rootleaf(root.right)
    #     return root.val + l if l < r else root.val + r


    # Another Approach with Global Parameter
    def tree_minpathsum_rootleaf(self, root):
        # Write your code here
        self.minimum = float('inf')
        self.dfs_minrootleaf(root)
        return self.minimum
        
    def dfs_minrootleaf(self, node, total=0):
        if node and not node.left and not node.right:
            self.minimum = min(self.minimum, total + node.val)
        
        if node.left:    
            self.dfs_minrootleaf(node.left, total + node.val)
        if node.right:
            self.dfs_minrootleaf(node.right, total + node.val)


    """
    @param root: The root of a Binary Tree
    @return: A Integer denotes as maximum sum
    Path means anynode to anynode
    """
    # # Normal Approach with DFS
    # def tree_maxsumpath_anywhere(self, root):
    #     total, single = self.dfs_maxanywhere(root)
    #     return total

    # def dfs_maxanywhere(self, root):
    #     if not root: return float('-inf'), 0
        
    #     ltotal, lsingle = self.dfs_maxanywhere(root.left)
    #     rtotal, rsingle = self.dfs_maxanywhere(root.right)

    #     single = max(root.val + max(lsingle, rsingle), 0)
    #     total = max(ltotal, rtotal, lsingle,+rsingle+root.val)

    #     return total, single


    # Another Approach with Global Parameter
    def tree_maxpathsum_anywhere(self, root):
        # write your code here
        self.maximum = root.val if root else 0
        self.dfs_maxanywhere(root)
        return self.maximum

    def dfs_maxanywhere(self,root):
        if root==None: return 0
        lsingle,rsingle = self.dfs_maxanywhere(root.left), self.dfs_maxanywhere(root.right)
        single =max(root.val,root.val+max(lsingle,rsingle))
        self.maximum = max(self.maximum, single ,root.val+lsingle+rsingle)
        return single


    """
    @param root: The root of a Binary Tree
    @return: A Integer denotes as maximum sum
    Path means from root to anynode
    """
    # Because from root, we can use max(result) 
    # result is a list of all node with sum info
    def tree_maxpathsum_fromroot(self, root):
        result = []
        self.dfs_maxfromroot(root, 0, result)
        return max(result)
    
    def dfs_maxfromroot(self, node, total, result):
        result.append(total+node.val)
        if node.left: self.dfs_maxfromroot(node.left, total+node.val, result)
        if node.right: self.dfs_maxfromroot(node.right, total+node.val, result)


    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def tree_continue_rootleaf(self, root):
        return self._dfs_continue_rootleaf(root, None, 0)
    
    def _dfs_continue_rootleaf(self, curt, prev, count):
        if not curt: return 0
        
        total = count+1 if prev and prev.val+1 == curt.val else 1
        lcount = self._dfs_continue_rootleaf(curt.left, curt, total)
        rcount = self._dfs_continue_rootleaf(curt.right, curt, total)

        return max(total, lcount, rcount)


    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def tree_continue_anywhere(self, root):
        count, up, down = self._dfs_continue_anywhere(root)
        return count
    
    def _dfs_continue_anywhere(self, root):
        if not root: return 0, 0, 0
        
        lcount, lup, ldown = self._dfs_continue_anywhere(root.left)
        rcount, rup, rdown = self._dfs_continue_anywhere(root.right)

        count, up, down = 0, 0, 0
        if root.left and root.left.val+1 == root.val:
            up = max(up, lup+1)
        if root.right and root.right.val-1 == root.val:
            down = max(down, ldown+1)
        if root.left and root.left.val+1 == root.val:
            up = max(up, rup+1)
        if root.right and root.right.val-1 == root.val:
            down = max(down, rdown+1)
        count = max(up+down+1, lcount, rcount)

        return count, up, down




class TreeValid:
    """
    @param A: the root of binary tree a.
    @param B: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def valid_same_tree(self, A, B):
        if not A and not B: return True
        if not A or not B: return False
        if A.val != B.val: return False
        
        l = self.valid_same_tree(A.left, B.left)
        r = self.valid_same_tree(A.right, B.right)
        return l and r


    """
    @param A: the root of binary tree a.
    @param B: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def valid_tweak_tree(self, A, B):
        if not A and not B: return True
        if not A or not B: return False
        if A.val != B.val: return False
        
        ll = self.valid_tweak_tree(A.left, B.left)
        rr = self.valid_tweak_tree(A.right, B.right)
        lr = self.valid_tweak_tree(A.left, B.right)
        rl = self.valid_tweak_tree(A.right, B.left)
        return ll and rr or lr and rl


    """
    @param root: The root of a given tree
    @return: A boolean wheter it is mirror to itself
    """
    # Approcach with Recursion
    def valid_mirror_tree(self, root):
        if not root: return True
        A, B = root.left, root.right
        if not A and not B: return True
        if not A or not B: return False
        if A.val != B.val: return False
        
        inner = self.valid_mirror_tree(A.left) == self.valid_mirror_tree(B.right)
        outer = self.valid_mirror_tree(A.right) == self.valid_mirror_tree(B.left)
        return inner and outer

    # # Another approach with DFS
    # def valid_mirror_tree(self, root):
    #     if not root: return True
    #     return self.dfs_mirror(root.left, root.right)
    
    # def dfs_mirror(self, A, B):
    #     if not A and not B: return True
    #     if not A or not B: return False
    #     if A.val != B.val: return False
        
    #     inner = self.dfs_mirror(A.left, B.right)
    #     outer = self.dfs_mirror(A.right, B.left)
    #     return inner and outer


    """
    @param root: the root of binary tree.
    @return: true if it is a complete binary tree, or false.
    """
    def valid_complete_tree(self, root):
        if not root: return True
        
        queue = [root]
        for item in queue:
            if item: queue.extend([item.left, item.right])
        
        for idx in range(len(queue))[::-1]:
            if queue[idx] == None: queue.pop()
        
        for item in queue:
            if item == None: return False
        
        return True


    """
    @param root: The root of a given tree
    @return: A boolean wheter it is a valid BST
    """
    # Method 1: Recursion
    def valid_bst_recursion(self, root):
        return self.dfs_bst(root, None, None)
    
    def dfs_bst(self, node, left, right):
        if not node: return True
        if not ((not left or left < node.val) and (not right or node.val < right)): return False
        return self.dfs_bst(node.left, left, node.val) and self.dfs_bst(node.right, node.val, right)

    
    # Method 2: Iteration (Inorder) with sorted(set(result)) == result
    def valid_bst_iteration(self, root):
        result, stack = [], []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            result.append(root.val)
            root = root.right
        
        return sorted(set(result)) == result  




class TreeTraverse:
    """
    @param root: The root of binary tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder(self, root):
        self.rank, stack = [], [(root, False)]
        while stack:
            node, visit = stack.pop()
            if not node: continue
            if visit: self.rank.append(node.val)
            else: stack.extend([(node.right, False), (node, True), (node.left, False)])
        return self.rank


    """
    @param root: The root of binary tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder(self, root):
        self.rank, stack = [], [(root, False)]
        while stack:
            node, visit = stack.pop()
            if not node: continue
            if visit: self.rank.append(node.val)
            else: stack.extend([(node.right, False), (node.left, False), (node, True)])
        return self.rank


    """
    @param root: The root of binary tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder(self, root):
        self.rank, stack = [], [(root, False)]
        while stack:
            node, visit = stack.pop()
            if not node: continue
            if visit: self.rank.append(node.val)
            else: stack.extend([(node, True), (node.right, False), (node.left, False)])
        return self.rank


    """
    @param root: The root of binary tree
    @return: Level order in ArrayList which contains node values.
    """
    def levelorder(self, root):
        self.rank, queue = [], [root]
        if not root: return self.rank
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            self.rank.append(level)
        return self.rank


    """
    @param root: The root of binary tree
    @return: Zigzagorder in ArrayList which contains node values.
    """
    def zigzagorder(self, root):
        self.rank, queue, flag = [], [root], False
        if not root: return self.rank
        while queue:
            level, flag = [], not flag
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            self.rank = self.rank+[level] if flag else self.rank+[level[::-1]]
        return self.rank
            


    """
    @param root: The root of binary tree
    @return: Verticalorder in ArrayList which contains node values.
    """
    def verticalorder(self, root):
        scale, queue = defaultdict(list), deque()
        queue.append((root, 0))
        while queue:
            node, i = queue.popleft()
            if node:
                scale[i].append(node.val)
                queue.extend([(node.left, i-1), (node.right, i+1)])
        return [scale[i] for i in sorted(scale)]     


    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def collect_tree_paths(self, root):
        result = []
        self.dfs_tree_paths(root, [], result)
        return result

    def dfs_tree_paths(self, root, path, result):
        if not root: return 

        path.append(root.val)
        if not root.left and not root.right:
            level = [str(val) for val in path]
            text = '->'.join(level)
            result.append(text)
        
        # Must be deep copy instead of shallow copy
        self.dfs_tree_paths(root.left, path[:], result)
        self.dfs_tree_paths(root.right, path[:], result)


    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves into a List of Lists
    """
    def collect_tree_leaves(self, root):
        result = []
        self.dfs_tree_leaves(root, result)
        return result
    
    def dfs_tree_leaves(self, node, result):
        if not node: return 0
        
        l = self.dfs_tree_leaves(node.left, result)
        r = self.dfs_tree_leaves(node.right, result)
        depth = max(l, r) + 1

        if depth-1 < len(result):
            result[depth-1].append(node.val)
        else:
            result.append([node.val])

        return depth




class TreeSearch:
    """
    @param: root: the root of tree
    @return: the max node
    """
    # Also useful for 2nd, kth largest/smallest/closest element
    def find_max_node(self, root):
        result, stack = [], []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            result.append(root.val)
            root = root.right
        
        return max(result)   


    """
    @param root: The root of the given tree
    @param k: An integer as a target in the tree
    @return: The value of the nearest leaf node to target k in the tree
    """
    def find_closest_leaf(self, root, k):
        if not root: return None

        node = TreeNode(root.val)
        self._connect_tree(root, node)
        k_node = self._search_leaf(node, k)
        queue, visit = [k_node], set([k_node])

        while queue:
            for i in range(len(queue)):
                curt = queue.pop(0)
                if not curt: 
                    return 'No such val in this tree.'
                if not curt.left and not curt.right:
                    return curt.val
                if curt.left and curt.left not in visit:
                    queue.append(curt.left)
                    visit.add(curt.left)
                if curt.right and curt.right not in visit:
                    queue.append(curt.right)
                    visit.add(curt.right)
                if curt.parent and curt.parent not in visit:
                    queue.append(curt.parent)
                    visit.add(curt.parent)
        return None

    def _connect_tree(self, root, node):
        if not root.left and not root.right:
            return 

        if root.left:
            lnode = TreeNode(root.left.val)
            lnode.parent, node.left = node, lnode
            self._connect_tree(root.left, lnode)
        if root.right:
            rnode = TreeNode(root.right.val)
            rnode.parent, node.right = node, rnode
            self._connect_tree(root.right, rnode)

    def _search_leaf(self, node, k):
        if not node: return None
        if k == node.val: return node
        
        lnode = self._search_leaf(node.left, k)
        rnode = self._search_leaf(node.right, k)

        if lnode: return lnode
        if rnode: return rnode
        return None


    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    A, B must in the tree
    """
    def tree_lca_recursion(self, root, A, B):
        if not root or root == A or root == B: return root
        lnode = self.tree_lca_recursion(root.left, A, B)
        rnode = self.tree_lca_recursion(root.right, A, B)

        if lnode and rnode: return root
        elif lnode: return lnode
        elif rnode: return rnode
        else: return None


    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    A, B must in the tree
    """        
    def tree_lca_parent(self, root, A, B):
        record = dict()
        while A is not root:
            record[A] = True
            A = A.parent
        
        while B is not root:
            if B in record: return B
            B = B.parent
        
        return root          


    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def tree_lca_general(self, root, A, B):
        node, a, b = self.dfs_lca_general(root, A, B)
        return node if a and b else None

    def dfs_lca_general(self, root, A, B):
        if not root: return None, False, False

        lnode, la, lb = self.dfs_lca_general(root.left, A, B)
        rnode, ra, rb = self.dfs_lca_general(root.right, A, B)

        a = la or ra or A == root
        b = lb or rb or B == root

        if A == root or B == root: return root, a, b
        if lnode and rnode: return root, a, b
        elif lnode: return lnode, a, b
        elif rnode: return rnode, a, b
        else: return None, a, b # None, False, Flase   also work

  
    """
    @param root: the root of binary tree
    @return: the root of the maximum subtree
    """
    def subtree_max_sum(self, root):
        node, total, large = self.dfs_max_sum(root)
        return node.val
    
    def dfs_max_sum(self, root):
        if not root: return None, 0, float('-inf')
        
        lnode, ltotal, llarge = self.dfs_max_sum(root.left)
        rnode, rtotal, rlarge = self.dfs_max_sum(root.right)
        node, total, large = root, root.val+rtotal+ltotal, root.val+rtotal+ltotal

        if llarge > large: node, large = lnode, llarge
        if rlarge > large: node, large = rnode, rlarge
        
        return node, total, large

    
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def subtree_min_sum(self, root):
        node, total, small = self.dfs_min_sum(root)
        return node.val
    
    def dfs_min_sum(self, root):
        if not root: return None, 0, float('inf')
        
        lnode, ltotal, lsmall = self.dfs_min_sum(root.left)
        rnode, rtotal, rsmall = self.dfs_min_sum(root.right)
        node, total, small = root, root.val+rtotal+ltotal, root.val+rtotal+ltotal

        if lsmall <= small: node, small = lnode, lsmall
        if rsmall <= small: node, small = rnode, rsmall
        
        return node, total, small


    """
    @param root: the root of binary tree
    @return: the root of the maximum average subtree
    """
    def subtree_max_avg(self, root):
        node, total, size, maxavg = self.dfs_max_avg(root)
        return node.val
    
    def dfs_max_avg(self, root):
        if not root: return None, 0, 0, float('-inf')

        lnode, ltotal, lsize, lmaxavg = self.dfs_max_avg(root.left)
        rnode, rtotal, rsize, rmaxavg = self.dfs_max_avg(root.right)
        node, total = root, root.val+ltotal+rtotal
        size, maxavg = 1+lsize+rsize, total/(1+lsize+rsize)

        if lmaxavg > maxavg: node, maxavg = lnode, lmaxavg
        if rmaxavg > maxavg: node, maxavg = rnode, rmaxavg

        return node, total, size, maxavg


    """
    @param root: the root of binary tree
    @return: the root of the minimum average subtree
    """
    def subtree_min_avg(self, root):
        node, total, size, minavg = self.dfs_min_avg(root)
        return node.val
    
    def dfs_min_avg(self, root):
        if not root: return None, 0, 0, float('inf')

        lnode, ltotal, lsize, lminavg = self.dfs_min_avg(root.left)
        rnode, rtotal, rsize, rminavg = self.dfs_min_avg(root.right)
        node, total = root, root.val+ltotal+rtotal
        size, minavg = 1+lsize+rsize, total/(1+lsize+rsize)

        if lminavg <= minavg: node, minavg = lnode, lminavg
        if rminavg <= minavg: node, minavg = rnode, rminavg

        return node, total, size, minavg


    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: List of all valid paths Lists
    Path means from root to leaf node
    """
    def tree_pathsum_rootleaf(self, root, target):
        result = []
        self.dfs_rootleaf(root, target, [], result)
        return result

    def dfs_rootleaf(self, node, target, path, result):
        if not node: return 
        elif not node.left and not node.right and node.val == target:
            return result.append(path+[node.val])

        self.dfs_rootleaf(node.left, target-node.val, path+[node.val], result)
        self.dfs_rootleaf(node.right, target-node.val, path+[node.val], result)


    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: List of all valid paths Lists
    Path means anynode to anynode downward
    """
    # Approach: Check Subtree in Main Function with DFS/Stack and then DFS
    # Traverse with any methods: Preorder, Inorder, Postorder, Level...
    def tree_pathsum_downward(self, root, target):
        result, stack, curt = [], [], root
        while stack or curt:
            while curt:
                stack.append(curt)
                curt = curt.left
            curt = stack.pop()
            # result.append(curt.val)
            self.dfs_downward(curt, target, [], result)
            curt = curt.right
        return result

    def dfs_downward(self, node, target, path, result):
        if not node: return
        # return 可写可不写 path或path[:]都可以
        if node.val == target: return result.append(path+[node.val])

        self.dfs_downward(node.left, target-node.val, path+[node.val], result)
        self.dfs_downward(node.right, target-node.val, path+[node.val], result) 
        

    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: List of all valid paths Lists
    Path means anynode to anynode
    Parent attribute in TreeNode
    """
    def tree_pathsum_anywhere(self, root, target):
        result, queue = [], [root]
        while queue and root:
            curt = queue.pop(0)
            if curt.left: queue.append(curt.left)
            if curt.right: queue.append(curt.right)
            self.dfs_anywhere(curt, None, target, [], result)
        return result

    def dfs_anywhere(self, node, father, target, path, result):
        if not node: return 
        if target == node.val: result.append(path+[node.val])
        
        # Top-Down Path
        if node.left not in [None, father]: 
            self.dfs_anywhere(node.left, node, target-node.val, path+[node.val], result)
        if node.right not in [None, father]: 
            self.dfs_anywhere(node.right, node, target-node.val, path+[node.val], result)
        # Bottom-Up Path
        if node.parent not in [None, father]: 
            self.dfs_anywhere(node.parent, node, target-node.val, path+[node.val], result)




class TreeOperate:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    """
    def serialization(self, root):
        data, queue = '', [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                data += str(node.val) + ','
                queue.extend([node.left, node.right])
            else:
                data += '#,'
        
        return data

    """
    @param data: A string serialized by your serialize method.
    """
    def deserialization(self, data):
        queue, head = [], None
        data = data[:-1].split(',')

        if data[0] != '#':
            root = TreeNode(int(data[0]))
            queue.append(root)

        i = 1
        while i < len(data):
            node = queue.pop(0)
            if node:
                if data[i] != '#':
                    node.left = TreeNode(int(data[i]))
                queue.append(node.left)
                i += 1
                if data[i] != '#':
                    node.right = TreeNode(int(data[i]))
                queue.append(node.right)
                i += 1
        
        return root




    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def tree_to_fakelinklist(self, root):
        if not root: return root
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            
            node.left = None
            node.right = stack[-1] if stack else None
        
        return root


    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bst_to_doublylinklist(self, root):
        dummy = head = ListNode(0)
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            node = ListNode(root.val)
            head.next, node.prev = node, head
            head, root = head.next, root.right

        return dummy.next


    """
    @param root: the root of binary tree
    @return: new root
    """
    # Recursion Approach
    def upsidedown_recursion(self, root):
        if not root or not root.left: return root
        
        left, right = root.left, root.right
        new_root = self.upsidedown_recursion(left)
        left.left, left.right = right, root
        root.left, root.right = None, None

        return new_root

    # Iteration Approach
    def upsidedown_iteration(self, root):
        left = right = None
        while root != None:
            newroot = root.left
            root.left = right
            right = root.right
            root.right = left
            left = root
            root = newroot
        return left


    """
    @param root: The root of a tree
    @return: Nothing but connect node with its parent
    """
    def connect_parent_tree(self, root):
        self.dfs_connect_parent(root, root)
    
    def dfs_connect_parent(self, root, node):
        if not root.left and not root.right:
            return 

        if root.left:
            lnode = TreeNode(root.left.val)
            lnode.parent, node.left = node, lnode
            self.dfs_connect_parent(root.left, lnode)
        if root.right:
            rnode = TreeNode(root.right.val)
            rnode.parent, node.right = node, rnode
            self.dfs_connect_parent(root.right, rnode)


    """
    @param root: The root of a tree
    @param val1: 1st value need to be swap
    @param val2: 2nd value need to be swap
    @return: Nothing but swap two values in the tree
    """
    # def swap(self, root, v1, v2):
    #     record = self.inorder(root)
    #     if v1 not in record or v2 not in record: return root
    #     i1, i2 = record.index(v1), record.index(v2)
    #     record[i1], record[i2] = v2, v1
    #     bst_swap = BST()
    #     for v in record: bst_swap.build(v)
    #     return bst_swap.root

    


class TreeVisualize:
    """
    @param root: The root of a tree
    @return: Void but visualize the tree structure
    """
    def tree_visulaization(self, root):
        ### Get Height of the tree
        height = self._get_tree_height(root)
        # print(height)

        # print(root)
        ### Deepcopy the tree
        self.root_copy = deepcopy(root)
        # print(self.root_copy)


        ### Populate Tree into a Complete Tree -- Fill None Node with " " 
        self._populate_tree(self.root_copy, height)
        root_visualize = self.root_copy
        # print(root_visualize)


        ### Visualize Tree Layer by Layer
        ### Each Layer include Node Level and Edge Level
        ## Node Level -- Node Value with/without Dashes
        ## Edge Level -- Edge (/ or \) connect Node/Dash
        queue, depth = [root_visualize], 1
        while queue:
            copy = []
            while queue:
                item = queue.pop(0)
                # print(item)
                copy.append(item)

            # Initiate Level String and Edges String
            edges_string            = ""
            level_string            = ""
            # Initiate Toggle Variables for Node Level
            first_item_in_level     = True
            extra_space_next_node   = False



            while copy:
                node = copy.pop(0)
                

                # Initiate Spacing for This Level:
                base_number  = 2
                init_padding = 2

                spaces_add = 0
                spaces_pre = pow(base_number, height-depth+1) - 1
                spaces_mid = pow(base_number, height-depth+2) - 2
                dash_count = pow(base_number, height-depth) - 2

                dash_count = max(dash_count, 0)
                spaces_mid -= (dash_count * init_padding)
                spaces_pre -= (dash_count - init_padding)
                
                if first_item_in_level: 
                    edges_string += " " * init_padding


                ## Construct Edge String in this Layer:
                edge_element = "/" if node.left and node.left.val is not " " else " "
                if first_item_in_level:
                    edges_string += " " * (pow(base_number, height-depth) - 1) + edge_element
                else:
                    edges_string += " " * (pow(base_number, height-depth+1) + 1) + edge_element

                edge_element = "\\" if node.right and node.right.val is not " " else " "
                edges_string += " " * (pow(base_number, height-depth+1) - 3) + edge_element




                ## Construct Level String in this Layer
                # Calculate Dash Count:
                dash_left = " " if node.left and node.left.val == " " else "_"
                dash_right = " " if node.right and node.right.val == " " else "_"


                # Calculate Extra Space:
                if extra_space_next_node:
                    spaces_add = 1
                    extra_space_next_node = False


                # Handle Longer Node Value:
                data_length = len(str(node.val))
                if data_length > 1:
                    # Odd Case:
                    if data_length % 2 == 1:
                        # First Take Dash Space
                        if dash_count > 0:
                            dash_count -= ((data_length-1) // 2)
                        # Then Use Existing Space
                        else:
                            spaces_mid -= (data_length-1) // 2
                            spaces_pre -= (data_length-1) // 2
                        # Final Add Extra Space
                            if data_length != 1:
                                extra_space_next_node = True
                    # Even Case:
                    else:
                        # First Take Dash Space and Request Extra Space
                        if dash_count > 0:
                            dash_count -= ((data_length)//2 + 1)
                            extra_space_next_node = True
                        # Then Use Existing Space
                        else:
                            spaces_mid -= (data_length-1)
                            spaces_pre -= (data_length-1)


                #- Print Level String consist of Node Value with/without Dashes:
                level_string = ""
                if first_item_in_level:
                    level_string += (" " * spaces_pre)
                    level_string += (dash_left * dash_count)
                    level_string += str(node.val)
                    level_string += (dash_right * dash_count)
                    print(level_string, end=" ")

                    first_item_in_level = False

                else:
                    level_string += (" " * (spaces_mid - spaces_add))
                    level_string += (dash_left * dash_count)
                    level_string += str(node.val)
                    level_string += (dash_right * dash_count)
                    print(level_string, end=" ")

                # Adding Node for next Level String in the Queue
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            
            #- Print Edge String for this level Node-Dash String
            if queue: print("\n", edges_string)
            depth += 1

        
        # End of Tree Visualization
        print("\n") 




    def _get_tree_height(self, node):
        if not node: return 0

        l = self._get_tree_height(node.left)
        r = self._get_tree_height(node.right)
        
        return max(l, r) + 1




    def _populate_tree(self, node, height):
        if height <= 1: return node
        if node:
            empty_node = TreeNode(" ")
            if not node.left: node.left = empty_node
            if not node.right: node.right = empty_node
            self._populate_tree(node.left, height-1)
            self._populate_tree(node.right, height-1)




    # def tree_visualization(self, root):
    #     matrix = self._tree_level_matrix(root)
    #     print(len(matrix))
    #     print(matrix)
        
    # def _tree_level_matrix(self, root):
    #     matrix, queue = [], [root]
        
    #     while queue:
    #         level = ''
    #         for _ in range(len(queue)):
    #             node = queue.pop(0)
    #             if node:
    #                 level += str(node.val) + ','
    #                 queue.extend([node.left, node.right])
    #             else:
    #                 level += '#,'
    #         matrix += [level]
        
    #     return matrix












if __name__ == '__main__':
    print('Welcome to Smart Tree Library: \n\n')
    visualization = TreeVisualize()




    print('BT Initiating', end='  ==>>  ')
    rank = [4, 5, 7, 8, 10, 11, 13, 15, 17, 19]
    inorder = [4, 5, 7, 8, 10, 11, 13, 15, 17, 19]
    preorder = [10, 5, 4, 7, 8, 15, 11, 13, 17, 19]
    postorder = [4, 8, 7, 5, 13, 11, 19, 17, 15, 10]
    bt = BT(rank=rank, inorder=inorder, preorder=preorder, postorder=postorder)
    root_in_pre = bt.build_inorder_preorder(inorder=inorder, preorder=preorder)
    root_in_post = bt.build_inorder_postorder(inorder=inorder, postorder=postorder)
    root_max_val = bt.build_maxorder(rank=rank)
    print('BT Constructed!')


    print('You may compared the BT recovered from different order list -- Shoud be the same:')
    print('Visualize BT Structure Recover from Inorder and Preorder: \n')
    visualization.tree_visulaization(root_in_pre) 
    print('Visualize BT Structure Recover from Inorder and Posorder: \n')
    visualization.tree_visulaization(root_in_post)


    # print('BT Iterator:')
    iterator_in_pre = TreeIterator(root_in_pre)    
    iteration_in_pre = []
    while iterator_in_pre.has_next(): 
        iteration_in_pre += [str(iterator_in_pre.next_node().val)]
    print('Build with Inorder and Preorder: \n', '~>'.join(iteration_in_pre))

    iterator_in_post = TreeIterator(root_in_post)    
    iteration_in_post = []
    while iterator_in_post.has_next(): 
        iteration_in_post += [str(iterator_in_post.next_node().val)]
    print('Build with Inorder and Postorder: \n', '~>'.join(iteration_in_post))

    iterator_max_val = TreeIterator(root_max_val)    
    iteration_max_val = []
    while iterator_max_val.has_next(): 
        iteration_max_val += [str(iterator_max_val.next_node().val)]
    print('Build each root with max value: \n', '~>'.join(iteration_max_val))


    print('\n')




    print('BST Initiating', end=' ==>> ')
    bst = BST()
    input = [10, 5, 4, 1, 2, 15, 11, 17, 20, 19, 3, 7, 8, 13, 21]
    for v in input: bst.build(v)
    print('BST Constructed!')


    # print('BST Iterator:')
    root = bst.root
    iterator = TreeIterator(root)


    print('Visualize BST Structure in original construction: \n')
    visualization.tree_visulaization(root) 

    
    iteration_list = []
    while iterator.has_next(): 
        iteration_list += [str(iterator.next_node().val)]
    print('Normal Iteration: \n', '~>'.join(iteration_list))

    root_remove = bst.remove(root, 21)
    iterator_remove = TreeIterator(root_remove)
    iteration_list_remove = []
    while iterator_remove.has_next(): 
        iteration_list_remove += [str(iterator_remove.next_node().val)]
    print('Iteration after Remove: \n', '~>'.join(iteration_list_remove))

    root_trim = bst.trim(root, [4, 19])
    iterator_trim = TreeIterator(root_trim)
    iteration_list_trim = []
    while iterator_trim.has_next(): 
        iteration_list_trim += [str(iterator_trim.next_node().val)]
    print('Iteration after Trim: \n', '~>'.join(iteration_list_trim))


    print('Visualize BST Structure after delete and trim operation: \n')
    visualization.tree_visulaization(root)


    print('\n\n')




    print('Tree Validation:')
    valid = TreeValid()
    print('Is it a symmetric tree? \t', valid.valid_mirror_tree(root))
    print('Is it a completed tree? \t', valid.valid_complete_tree(root))
    print('Is it a valid BST? \t\t', valid.valid_bst_recursion(root))
    print('Is it a valid BST? \t\t', valid.valid_bst_iteration(root))
    print('Are two trees identical? \t', valid.valid_same_tree(root, root))
    print('Are two trees tweaked? \t\t', valid.valid_tweak_tree(root, root))


    print('\n')




    print('BST Basic Values:')
    attribute = TreeAttribute()
    print('Node Count of the Tree: \t', attribute.tree_node_count(root))
    print('Max Depth of the Tree: \t\t', attribute.tree_max_depth(root))
    print('Min Depth of the Tree: \t\t', attribute.tree_min_depth(root))
    print('Paths Sum of the Tree: \t\t', attribute.tree_paths_sum(root))
    print('Leaf Sum of the Tree: \t\t', attribute.tree_leaf_sum(root))
    print('Level Sum of the Tree: \t\t', attribute.tree_level_sum(root, 3))
    print('Longest Continue Path RootLeaf: ', attribute.tree_continue_rootleaf(root))
    print('Longest Continue Path Anywhere: ', attribute.tree_continue_anywhere(root))
    print('Min Path Sum RootLeaf: \t\t', attribute.tree_minpathsum_rootleaf(root))
    print('Max Path Sum Anywhere: \t\t', attribute.tree_maxpathsum_anywhere(root))
    print('Max Path Sum FromRoot: \t\t', attribute.tree_maxpathsum_fromroot(root))


    print('\n')




    print('Traversal of BST:')
    traverse = TreeTraverse()
    print('Traverse Inorder: \n', traverse.inorder(root))
    print('Traverse Preorder: \n', traverse.preorder(root))
    print('Traverse Postorder: \n', traverse.postorder(root))
    print('Traverse Levelorder: \n', traverse.levelorder(root))
    print('Traverse ZigZagorder: \n', traverse.zigzagorder(root))
    print('Traverse Verticalorder: \n', traverse.verticalorder(root))
    print('Tree Paths Collections: \n', traverse.collect_tree_paths(root))
    print('Tree Leaves Collections: \n', traverse.collect_tree_leaves(root))


    print('\n')




    print('Search in BST:')
    search = TreeSearch()
    print('Max Value in the Tree: \t\t', search.find_max_node(root))
    print('Leaf Value cloest to Target: \t', search.find_closest_leaf(root, 5))
    print('Max Sum Subtree Root Value: \t', search.subtree_max_sum(root))
    print('Min Sum Subtree Root Value: \t', search.subtree_min_sum(root))
    print('Max Avg Subtree Root Value: \t', search.subtree_max_avg(root))
    print('Min Avg Subtree Root Value: \t', search.subtree_min_avg(root))
    print('BST Lowest Common Ancestor: \t', 
          search.tree_lca_recursion(root, root.left.left, root.left.right).val)
    print('BST Lowest Common Ancestor: \t', 
          search.tree_lca_general(root, root.left.left, None))
    print('Search Target Paths RootLeaf: \n', search.tree_pathsum_rootleaf(root, 19))
    print('Search Target Paths Downward: \n', search.tree_pathsum_downward(root, 19))
    print('Search Target Paths Anywhere: \n', search.tree_pathsum_anywhere(root, 19))


    print('\n\n')




    print('Operation on BST:')
    operation = TreeOperate()


    print('Serialization and Deserialization: ')
    data_encode = operation.serialization(root)
    print('String from Tree Serialization: \n', data_encode)

    root_decode = operation.deserialization(data_encode)
    iterator_decode = TreeIterator(root_decode)
    iteration_list_decode = []
    while iterator_decode.has_next(): 
        iteration_list_decode += [str(iterator_decode.next_node().val)]
    print('Iteration from Deserializaion: \n', '~>'.join(iteration_list_decode))


    print('\n')


    print('Convert to other Data Structure: ')
    bst_list = []
    root_head = operation.tree_to_fakelinklist(root)
    while root_head: 
        bst_list += [str(root_head.val)]
        root_head = root_head.right
    print('Convert to Fake Linked List: \n', '->'.join(bst_list))

    bst_dlist = []
    root_dhead = operation.bst_to_doublylinklist(root)
    while root_dhead:
        bst_dlist += [str(root_dhead.val)]
        root_dhead = root_dhead.next
    print('Convert to Doubly Linked List: \n', '<=>'.join(bst_dlist))


    print('\n')




    print('Upsidedown the Tree: ')
    print('BST Initiating', end=' ==>> ')
    bst = BST()
    input = [10, 5, 4, 15, 11, 17, 19, 7, 8, 13]
    for v in input: bst.build(v)
    print('BST Constructed!')

    root = bst.root



    print('Traverse before Upsidwon: \n', traverse.levelorder(root))

    print('Visualize BST Structure in original construction: \n')
    visualization.tree_visulaization(root) 
    
    root_upsidedown = operation.upsidedown_iteration(root)

    print('Traverse after Iteration Upsidown: \n', traverse.levelorder(root_upsidedown))
    
    print('Visualize BST Structure after Iteration Upsidown: \n')
    visualization.tree_visulaization(root_upsidedown) 




    print('BST Initiating', end=' ==>> ')
    bst = BST()
    input = [10, 5, 4, 15, 11, 17, 19, 7, 8, 13]
    for v in input: bst.build(v)
    print('BST Constructed!')

    root = bst.root


    print('Traverse before Upsidwon: \n', traverse.levelorder(root))

    print('Visualize BST Structure in original construction: \n')
    visualization.tree_visulaization(root) 

    root_downsideup = operation.upsidedown_recursion(root)

    print('Traverse after Recursion Upsidown: \n', traverse.levelorder(root_downsideup))
    print('Visualize BST Structure after Recursion Upsidown: \n')
    visualization.tree_visulaization(root_downsideup) 


    print('\n\n')

    


    # print('Connect Parent Node in the Tree')
    # print('\n')




    # print('Swap Two Nodes in the Tree')
    # print('\n')




    # print('BST Initiating', end=' ==>> ')
    # bst = BST()
    # input = [10, 5, 4, 1, 2, 15, 11, 17, 20, 19, 3, 7, 8, 13, 21]
    # for v in input: bst.build(v)
    # print('BST Constructed!')

    # root = bst.root
    # iterator = TreeIterator(root)
    
    # iteration_list = []
    # while iterator.has_next(): 
    #     iteration_list += [str(iterator.next_node().val)]
    # print('Normal Iteration: \n', '~>'.join(iteration_list))

    # print('Visualization of the Tree:')
    # tools = TreeTools()
    # tools.tree_visualization(root)
    # print('\n')





