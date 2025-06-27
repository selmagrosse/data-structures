from queue import Queue

class AVLTree:
    
    class Node:
        def __init__(self, value, left=None, right=None):
            self.bf = 0 # balance factor
            self.value = value
            self.height = 0
            # left and right children
            self.left = left
            self.right = right
            
    def __init__(self):
        self.node_count = 0
        self.root = None
        
    def height(self):
        if self.root is None:
            return 0
        return self.root.height
        
    def is_empty(self):
        """Check if the tree is empty."""
        return self.size() == 0
    
    def size(self):
        """Return the number of nodes in the tree."""
        return self.node_count
    
    def add(self, element):
        """Add an element to the tree. Return True if added, False if it already exists."""
        if element is None:
            return False
        if self.contains(element):
            return False
        else:
            self.root = self._add(self.root, element)
            self.node_count += 1
            return True
        
    def _add(self, node, element):
        if node is None:
            # add element to a leaf node
            node = self.Node(element)
        else:
            if element < node.value:
            # element is lower than the node value, therefore add to its left subtree
                node.left = self._add(node.left, element)
            else:
                node.right = self._add(node.right, element)
        self.update(node)
        return self.balance(node)
    
    def update(self, node):
        """Update node's height and balance factor"""
        # left node height init
        lh = -1
        # right node height init
        rh = -1
        if node.left is not None:
            lh = node.left.height
        if node.right is not None:
            rh = node.right.height
        node.height = 1 + max(lh, rh)
        node.bf = rh - lh
        
    def balance(self, node):
        # left heavy subtree
        if node.bf == -2:
            # left-left case
            if node.left.bf <= 0:
                return self.left_left(node)
            # left-right case
            else:
                return self.left_right(node)
            
        # right heavy subtree
        if node.bf == 2:
            # right-right case
            if node.right.bf >= 0:
                return self.right_right(node)
            # right-left case
            else:
                return self.right_left(node)
            
        return node
    
    def left_left(self, node):
        return self.right_rot(node)
    def left_right(self, node):
        node.left = self.left_rot(node.left)
        return self.left_left(node)
    
    def right_right(self, node):
        return self.left_rot(node)
    def right_left(self, node):
        node.right = self.right_rot(node.right)
        return self.right_right(node)
    
    def left_rot(self, node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        self.update(node)
        self.update(tmp)
        return tmp
    
    def right_rot(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        self.update(node)
        self.update(tmp)
        return tmp
    
    def contains(self, element):
        """Check if element exists in the tree."""
        return self._contains(self.root, element)
    
    def _contains(self, node, element):
        if node is None:
            return False
        if element < node.value:
            return self._contains(node.left, element)
        elif element > node.value:
            return self._contains(node.right, element)
        else:
            return True
        
    def remove(self, element):
        """Remove an element from the tree. Return True if removed, False if it does not exist."""
        if self.contains(element):
            self.root = self._remove(self.root, element)
            self.node_count -= 1
            return True
        return False
    
    def _remove(self, node, element):
        if node is None:
            return None
        # traverse the tree to find the element and remove it
        if element < node.value:
            # go into the left subtree
            node.left = self._remove(node.left, element)
        elif element > node.value:
            node.right = self._remove(node.right, element)
        else:
            # found the node we wish to remove
            # Case 1: no subtree or only right subtree
            if node.left is None:
                return node.right
            # Case 2: only left subtree
            elif node.right is None:
                return node.left
            # Case 3: both left and right subtrees exist
            else:
                # find the leftmost node in the right subtree
                tmp = self.dig_left(node.right)
                # swap data
                node.value = tmp.value
                node.right = self._remove(node.right, tmp.value)
        self.update(node)
        return self.balance(node)
    
    def dig_left(self, node):
        """Find the leftmost node in the subtree rooted at node."""
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur
    
    def dig_right(self, node):
        """Find the rightmost node in the subtree rooted at node."""
        cur = node
        while cur.right is not None:
            cur = cur.right
        return cur
    
    def traverse(self, order):
        """Traverse the binary search tree in the specified order."""
        """Supported orders: 'preorder', 'inorder', 'postorder', 'levelorder'."""
        if order == 'preorder':
            self.preorder(self.root)
        elif order == 'inorder':
            self.inorder(self.root)
        elif order == 'postorder':
            self.postorder(self.root)
        elif order == 'levelorder':
            self.levelorder(self.root)
            
    def preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)
        
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)
            
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)
        
    def levelorder(self, node):
        """Level order traversal using a queue."""
        if node is None:
            return
        queue = Queue(node)
        
        while not queue.is_empty():
            cur = queue.dequeue()
            print(cur.value)
            if cur.left:
                queue.enqueue(cur.left)
            if cur.right:
                queue.enqueue(cur.right) 

    def __repr__(self):
        """Return a string representation of the tree."""
        def recurse(node):
            if node is None:
                return 'None'
            return f'Node({node.value}, left={recurse(node.left)}, right={recurse(node.right)})'
        return recurse(self.root)