class DynamicArray:
    
    def __init__(self, capacity=1):
        if capacity < 0:
            raise BaseException("Array size less than 0! Enter valid array size.")
        self.array = [0] * capacity
        self.capacity = capacity # length user thinks the array is
        self.length = 0 # actual array size
        
    def size(self):
        return self.length
    
    def isEmpty(self):
        return self.size() == 0
    
    def get(self):
        return self.array[:self.length] # Return only valid elements
    
    def set(self, array):
        self.array = array[:]
        self.length = len(array)
        self.capacity = max(self.capacity, self.length)
        
    def clear(self):
        self.array = [None] * self.capacity
        self.length = 0
        
    def append(self, item):
        if self.length + 1 >= self.capacity:
            self._resize()
            
        self.array[self.length] = item
        self.length += 1
        
    def pop(self, index=-1):
        if index > self.length - 1 or index < -self.length:
            raise BaseException("Index out of bounds!")
        
        if index  < 0:  # convert to a positive index
           index += self.length
             
        value = self.array[index]
        
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i+1]
        
        self.length -= 1
        return value
    
    def remove(self, item):
        size = self.length
        for i in range(self.length):
            if self.array[i] == item:
                self.pop(i)
        if self.length < size:
            return True
        return False
    
    def find(self, item):
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1
    
    def contains(self, item):
        return self.find(item) != -1
    
    def insert(self, item, index):
        if index > self.length - 1 or index < -self.length:
            raise BaseException("Index out of bounds!")
            
        if self.length + 1 >= self.capacity:
            self._resize()
            
        if index  < 0:  # convert to a positive index
            index += self.length
        
        for i in range(self.length, index - 1, -1):
            self.array[i+1] = self.array[i]              
        
        self.array[index] = item
        self.length += 1
        
    def __repr__(self):
        return str(self.array[:self.length])
            
        
    def _resize(self):
        new_array = self.array[:]
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity *= 2
        self.array = [0] * self.capacity
        self.array[:self.length] = new_array
    
        

# main
# dyn_array = DynamicArray(4)
# dyn_array.set([1,2,3,4])

