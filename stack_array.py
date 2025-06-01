#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 17:44:42 2025

@author: selmamusic
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 15:54:47 2025

@author: selmamusic
"""

from dynamic_array import DynamicArray

class Stack:
    
    def __init__(self, element=None):
        self.array = DynamicArray()
        if element is not None:
            self.array.append(element)
        
    def size(self):
        return self.array.size()
    
    def is_empty(self):
        return self.array.is_empty()
    
    def push(self, element):
        self.array.append(element)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("The stack is empty!")
                
        return self.array.pop()
        
    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty!")
        return self.array[-1]
        
    def __iter__(self):
        return iter(self.array)
    
    def __repr__(self):
        return f', '.join(str(x) for x in self.array)

if __name__ == "__main__":
    stack = Stack(3)
print(stack)