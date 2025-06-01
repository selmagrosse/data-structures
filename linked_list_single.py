#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:12:41 2025

@author: selmamusic
"""

class SingleLinkedList:
    
    def __init__(self, size=0):
        self.size = size
        self.head = None
        self.tail = None
    
    class Node:
        def __init__(self, data, nxt=None):
            self.data = data
            self.next = nxt
        
    def length(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def clear(self):
        ## explicit clear
        # trav = self.head
        # while trav is not None:
        #     next_node = trav.next # save a reference to the node
        #     trav.data = None
        #     trav.next = None   # break the link
        #     trav = next_node
        # python clear (garbage collector will delete everything if we break the link of head and tail)
        self.head = None
        self.tail = None
        self.size = 0
        
    def __getitem__(self, index):
        if index < 0 or index > self.size - 1:
            raise IndexError("Index out of bounds!")
        pointer = self.head
        for i in range(index):
            pointer = pointer.next
            
        return pointer.data
    
    def __setitem__(self, index, value):
        if index < 0 or index > self.size - 1:
            raise IndexError("Index out of bounds!")
        pointer = self.head
        for i in range(index):
            pointer = pointer.next
        pointer.data = value
        
    def add_last(self, element):
        new_node = self.Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def add_first(self, element):   
        new_node = self.Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
        self.size += 1
    
    def peek_first(self):
        if self.is_empty():
            raise IndexError("Linked list is empty!")
        return self.head.data
    
    def peek_last(self):
        if self.is_empty():
            raise IndexError("Linked list is empty!")
        return self.tail.data
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Linked list is empty!")
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        
        return data
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Linked list is empty!")
        
        data = self.tail.data
        count = 0
        current = self.head
        while count < self.size - 1:
            current = current.next
            count += 1
        self.tail = current
        self.size -= 1
        if self.is_empty():
            self.tail = None
        
        return data
    
    def _remove(self, node):
        if node==self.head:
            return self.remove_first()
        if node==self.tail:
            return self.remove_last()
            
        pointer = self.head
        while pointer.next != node:
            pointer = pointer.next
        
        data = pointer.next.data
        pointer.next = node.next
        self.size -= 1
        
        return data
    
    def removeAt(self, index):
        if index < 0 or index > self.size - 1:
            raise IndexError("Index out of bounds!")
        if self.is_empty():
            raise IndexError("Linked list is empty!")
        
        pointer = self.head
        for i in range(index):
            pointer = pointer.next
        self._remove(pointer)
        
    def remove(self, value):
        if self.is_empty():
            raise IndexError("Linked list is empty!")
            
        pointer = self.head
        while pointer is not None and pointer.data != value:
            pointer = pointer.next
        
        if pointer:
            self._remove(pointer)
            return True
        else:
            return False
        
    def indexOf(self, value):
        # find the index of a particular value
        if self.is_empty():
            raise IndexError("Linked list is empty!")
        pointer = self.head
        for i in range(self.size):
            if pointer.data == value:
                return i
            pointer = pointer.next
        return -1
    
    def contains(self, value):
        return self.indexOf(value) != -1

    def reverse(self):
        if self.size==1:
            return self.head
        
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev
            
    
    def __iter__(self):
        pointer = self.head
        while pointer is not None:
            yield pointer.data
            pointer = pointer.next
            
    def __repr__(self):
        values = []
        pointer = self.head
        while pointer is not None:
            values.append(str(pointer.data))
            pointer = pointer.next
        return " ".join(values)

if __name__ == "__main__":
    sll = SingleLinkedList()