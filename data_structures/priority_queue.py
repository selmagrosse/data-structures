#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 24 11:45:07 2025

@author: selmamusic
"""

class PriorityQueue:
    
    def __init__(self, elements=None):
        self.heap = []
        self.map = {}
        
        if elements is not None:
            for element in elements:
                self.push(element)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def clear(self):
        self.heap.clear()
        self.map.clear()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]
    
    def contains(self, element):
        return element in self.map
    
    def poll(self):
        if self.is_empty():
            return None
        return self.remove_at(0)
        
    def push(self, element):
        if element is None:
            raise IndexError("No element provided.")
        if element in self.map:
            raise IndexError("Duplicate elements are not supported in this implementation.")
        self.heap.append(element)
        index = self.size() - 1
        self.map[element] = index
        self.bubble_up(index)
        
    def bubble_up(self, child_index):
        while child_index > 0:
            # get the parent by computing its index
            parent_index = (child_index - 1) // 2
            if self.heap[parent_index] < self.heap[child_index]:
                break
            self.swap(parent_index, child_index)
            child_index = parent_index
            
    def bubble_down(self, parent_index):
        
        while True:
            left_child = 2 * parent_index + 1
            right_child = 2 * parent_index + 2
            smallest = parent_index
              
            if left_child < self.size() and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child < self.size() and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
                
            if smallest == parent_index:
                break
                
            self.swap(parent_index, smallest)
            parent_index = smallest

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.map[self.heap[i]], self.map[self.heap[j]] = i, j
        
    def remove_at(self, index):
        if index >= self.size():
            return None
        
        removed_element = self.heap[index]
        self.swap(index, -1)
        self.heap.pop()
        del self.map[removed_element]
        
        self.bubble_up(index)
        self.bubble_down(index)
        
        return removed_element
    
    def remove(self, element):
        if element is None or element not in self.map:
            return False
        self.remove_at(self.map[element])
        return True
        
    def is_minheap(self, index):
        
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < self.size():
            if self.heap[index] > self.heap[left]:
                return False
            if not self.is_minheap(left):
                return False
        if right < self.size():
            if self.heap[index] > self.heap[right]:
                return False
            if not self.is_minheap(right):
                return False
    
        return True
    
    def __repr__(self):
        return ", ".join(str(item) for item in self.heap)
            
        

if __name__ == "__main__":
    pq = PriorityQueue()
    pq = PriorityQueue([1,2,0])