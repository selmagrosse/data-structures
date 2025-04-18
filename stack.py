#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 15:54:47 2025

@author: selmamusic
"""

from linked_list_double import DoubleLinkedList

class Stack:
    
    def __init__(self, element=None):
        self.dll = DoubleLinkedList()
        if element is not None:
            self.dll.add_first(element)
        
    def size(self):
        return self.dll.length()
    
    def is_empty(self):
        return self.dll.is_empty()
    
    def push(self, element):
        self.dll.add_last(element)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("The stack is empty!")
                
        return self.dll.remove_last()
        
    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty!")
        return self.dll.peek_last()
        
    def __iter__(self):
        return iter(self.dll)
    
    def __repr__(self):
        return f', '.join(str(x) for x in self.dll)
  
stack = Stack(3)
print(stack)