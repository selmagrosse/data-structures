#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 18:04:41 2025

@author: selmamusic
"""

from linked_list_double import DoubleLinkedList

class Queue:
    
    def __init__(self, element=None):
        self.dll = DoubleLinkedList()
        if element is not None:
            self.dll.add_first(element)
        
    def size(self):
        return self.dll.length()
    
    def is_empty(self):
        return self.dll.is_empty()
    
    def enqueue(self, element):
        self.dll.add_last(element)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty!")
                
        return self.dll.remove_first()
        
    def peek(self):
        if self.is_empty():
            raise IndexError("The queue is empty!")
        return self.dll.peek_first()
        
    def __iter__(self):
        return iter(self.dll)
    
    def __repr__(self):
        return f', '.join(str(x) for x in self.dll)

if __name__ == "__main__":
    queue = Queue(3)
    print(queue)