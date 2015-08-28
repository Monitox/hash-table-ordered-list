'''
Created on 31 May 2015

@author: sl0
'''
class Node:
    def __init__(self, info=0, next_=0):
        self._info = info
        self._next = next_

    def get_info(self):
        return self._info


    def get_next(self):
        return self._next


    def set_info(self, value):
        self._info = value


    def set_next(self, value):
        self._next = value

    info = property(get_info, set_info, None, None)
    next_ = property(get_next, set_next, None, None)

    