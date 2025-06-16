#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 11:38:49 2025

@author: selmamusic
"""

from queue import Queue

class BinarySearchTree:
    
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
            
    def __init__(self):
        self.node_count = 0
        self.root = None
        
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return self.node_count
    
    def add(self, element):
        if self.contains(self.root, element):
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
        return node
    
    def contains(self, node, element):
        if node is None:
            return False
        if element < node.value:
            return self.contains(node.left, element)
        elif element > node.value:
            return self.contains(node.right, element)
        else:
            return True
        
    def remove(self, element):
        if self.contains(self.root, element):
            self.root = self._remove(self.root, element)
            self.node_count -= 1
            return True
        return False
    
    def _remove(self, node, element):
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
        return node
    
    def dig_left(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur
    
    def dig_right(self, node):
        cur = node
        while cur.right is not None:
            cur = cur.right
        return cur
    
    def height(self, node):
        if node is None:
            return -1
        return max(self.height(node.left), self.height(node.right)) + 1
    
    def traverse(self, order):
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
    
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    bst.add(15)
    bst.add(3)
    bst.add(7)