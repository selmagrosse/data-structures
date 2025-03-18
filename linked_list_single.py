#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:12:41 2025

@author: selmamusic
"""

class SingleLinkedList:
    
    def __init__(self, size=0):
        self.size = size
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
    
    class Node:
        def __init__(self, data, nxt):
            self.data = data
            self.next = nxt
        
    def length(self):
        return self.size
    
    def isEmpty(self):
        return self.length() == 0
    
    def clear(self):
        trav = head
        while trav != None:
            trav.next = None
            trav.data = None
        self.head = None
        self.tail = None
        self.size = 0
        
    def add(self, element):
        self.tail.next = self.Node(element, None)
        self.tail = self.tail.next
        
    
    
    
# main
sll = SingleLinkedList()
#sll = SingleLinkedList(2, 1, 5)