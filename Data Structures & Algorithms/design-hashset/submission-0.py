class MyHashSet:

    def __init__(self):
         self.elements = []
        
    def add(self, key: int) -> None:
        if key not in self.elements:
            self.elements.append(key)

    def remove(self, key: int) -> None:
        if key in self.elements:            
            self.elements.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.elements


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)