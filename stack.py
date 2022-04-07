class EmptyException(Exception):
    def __init__(self,ADT_name):
        super().__init__(f"This {ADT_name} is empty.")

class Stack:
    def __init__(self,size = 1):
        self._data = [None] * size
        self._head = -1
        
    def __len__(self):
        return self._head + 1
    def is_empty(self):
        return self._head == -1       

    def push(self, item):
        if self.N == len(self):
            self._resize(self.N * 2)
        self._head += 1
        self._data[self._head] = item 
            
    def pop(self):
        if self.is_empty():
            raise EmptyException("Stack")
        temp = self._data[self._head]
        self._head -= 1
        
        if len(self) <= self.N * 0.4:
            self._resize(int(len(self)/2))
        return temp
    
    def top(self):
        if self.is_empty():
            raise EmptyException("Stack")
        return self._data[self._head]

    @property
    def N(self):
        return len(self._data)

    def _resize(self,cap):
        temp = [None] * cap
        temp[:len(self)] = self._data[:len(self)]
        self._data = temp
        
if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    
    while not stack.is_empty():
        print(stack.pop())