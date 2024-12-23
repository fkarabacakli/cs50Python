class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        
    def __str__(self):
        return f"🍪"*self.size

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1 :
            raise ValueError("Capacity must be bigger than 0")
        self._capacity = capacity
        

    @property
    def size(self):
        return self._size 
    
    @size.setter
    def size(self, size):
        if size > self._capacity or size < 0:
            raise ValueError("Size must be between 0 to Capacity.")
        self._size = size
    

def main():
    jar = Jar(20)
    jar.deposit(10)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(6)
    print(jar)


if __name__ == "__main__":
    main()