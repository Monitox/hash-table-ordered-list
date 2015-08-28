'''
Created on 1 Jun 2015

@author: sl0
'''
import copy

class OrderedListIterator:
    
    def __init__(self, ol):
        self._ol = ol
        self._crt = 0
        self._crt = self._merge_all_lists()
    
    def __iter__(self):
        return self
    
    def valid(self):
        if self._crt == 0:
            return False
        return True
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.valid() == False:
            raise StopIteration
        aux = self._crt.info
        self._crt = self._crt.next_
        return aux
    
    def element(self):
        return self._crt.info
    
    def _merge_lists(self, l1, l2):
        if self._ol._R(l1.info,  l2.info): #<
            head = l1
            l1 = l1.next_
        else:
            head = l2
            l2 = l2.next_
        llist = head
        while l1 != 0 and l2 != 0:
            if self._ol._R(l1.info, l2.info): #<
                llist.next_ = l1
                llist = llist.next_
                l1 = l1.next_
   
            else:
                llist.next_ = l2
                llist = llist.next_
                l2 = l2.next_
        while l1 != 0:
            llist.next_ = l1
            llist = llist.next_
            l1 = l1.next_
            
        while l2 != 0:    
            llist.next_ = l2
            llist = llist.next_
            l2 = l2.next_
            
        return head
   
    def _merge_all_lists(self):
        llist = 0
        for l1 in self._ol._table:
            if l1 != 0:
                if llist == 0:
                    llist = l1
                else:
                    llist = self._merge_lists(copy.deepcopy(llist), copy.deepcopy(l1))
        
        return llist

