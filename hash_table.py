class HashTable:
    def _init_(self, size=10):

     self.size = size
     self.table = [[] for _ in range (size)]
     self.count = 0


    def _hash(self, key):
       return key % self.size
    

    def _resize(self):
       new_size = self.size * 2
       new_table = [[] for _ in range (new_size) ]
       for bucket in self.table:
          for k, v in bucket:
             new_index = k % new_size
             new_table[new_index].append((k,v))
             self.size = new_size
       self.table = new_table

    def insert(self, key, value):
       
       if self.count / self.size > 0.7:
          self._resize()
          index = self._hash(key)
          for i,(k,v) in enumerate (self.table[index]):
             if k == key:
                self.table[index][i] = (key, value)
             return
          self.table[index].append((key, value))
       self.count += 1

    def search (self, key):
       index = self._hash(key)
       for k, v in self.table[index]:
          if k == key:
             return v
          return None
       
       def delete(self, key):
          index = self._hash(key)
          for i, (k,_) in enumerate (self.table[index]):
             if k == key:
                del self.table[index][i]
                self.count -= 1
                return True
             return False
          
          def display (self):
             for i, bucket in enumerate(self.table):
                print(f"Bucket {i}: {bucket if bucket else 'Empty'}")
       
