#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 15:17:49 2025

@author: selmagrosse
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.count = 0
        # init the hash table with a fixed size
        # create a list of buckets for chaining
        self.table = [[] for _ in range(size)]
        
    def __len__(self):
        return self.scount
    
    def is_empty(self):
        return self.count == 0
    
    def clear(self):
        self.table = [[] for _ in range(self.size)]
        self.size = 0
            
    def _hash(self, key):
        # generate an index for the given key using Py's hash function
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        # update value if key exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # add a new key-value pair to the chain
        self.table[index].append([key, value])
        self.count += 1
        
    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        # if the key is not found, raise an exception
        raise KeyError(f'Key {key} not found.')
    
    def delete(self, key):
        # remove a key-value pair
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0]==key:
                del self.table[index][i]
                self.count -= 1
                return
        raise KeyError(f'Key {key} not found.')
        
    def keys(self):
        keys = []
        for bucket in self.table:
            for pair in bucket:
                keys.append(pair[0])
        return keys
    
    def values(self):
        values = []
        for bucket in self.table:
            for pair in bucket:
                values.append(pair[1])
        return values
    
    def items(self):
        items = []
        for bucket in self.table:
            for pair in bucket:
                items.append(tuple(pair))
        return items
        
    def __contains__(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False
    
    def __iter__(self):
        for bucket in self.table:
            for pair in bucket:
                yield pair[0]
                
    def __getitem__(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f'Key {key} not found.')
        
    def __repr__(self):
        return '\n'.join(f'Index {i}: {bucket}' for i, bucket in enumerate(self.table))
        
if __name__ == "__main__":
    ht = HashTable(2)
    ht.insert('Selma', 1)
    ht.insert('Sebi', 2)
    ht.insert('Benjo', 3)
        
        
