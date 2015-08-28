'''
Created on 30 May 2015

@author: sl0
'''

from utils.constants import HASH_LEN
from hashlib import md5
from utils.node import Node
from utils.ordered_list_iterator import OrderedListIterator

class OrderedList:
  
    def __init__(self, rel = lambda x, y: x< y):
        self._table = [0] * HASH_LEN
        self._size = 0
        self._R = rel
        self._m = HASH_LEN
    
    def __iter__(self):
        return OrderedListIterator(self)
    
    def size(self):
        return self._size
    
    def insert(self, el):
        nod = Node(el, 0)
        pos = self._hash_code(el)
        if self._table[pos] == 0:
            self._table[pos] = nod
            self._size += 1
        else:
            p = self._table[pos]
            while p.next_ != 0 and self._R(nod.info, p.next_.info)==False:
                p = p.next_
            if p.next_ == 0:
                p.next_ = nod
                self._size += 1
            else:
                nod.next_ = p.next_
                p.next_ = nod
                self._size += 1
   
    def empty(self):
        if self._size == 0:
            return True
        return False
   
    def position(self, obj):
        if self.find(obj) == False:
            return -1;
        cnt = 0
        for o in self:
            if o == obj:
                return cnt
            cnt += 1
   
    def element(self, position):
        if position > self.size() or position < 0:
            raise IndexError("Position out of range!")
        pos = 0
        for o in self:
            if pos == position:
                return o
            pos+=1
    
    def __getitem__(self, index):
        return self.element(index)
    
    def _hash_code(self, obj):
        if type(obj) != int:
            key = obj.get_key()
        else: key = obj
        key.encode('utf-16')
        hash = md5(key.encode('utf-16'))
        hc = int(hash.hexdigest(), 16) % HASH_LEN
        return hc
    
    def erase(self, obj):
        if self.find(obj) == 0:
            raise ValueError("Cannot find object to erase!")
        index = self._hash_code(obj)

        p = self._table[index]
        
        if p.info == obj:
            self._table[index] = p.next_
            self._size -= 1 
        else:                    
            while p.next_.info != obj:
                p = p.next_
        
            p.next_ = p.next_.next_
            self._size -= 1
        
            
    def find(self, obj):
        index = self._hash_code(obj)
        if self._table[index] == 0:
            return False
        p = self._table[index]
        while p != 0:
            if p.info == obj:
                return True
            p = p.next_
        return False
