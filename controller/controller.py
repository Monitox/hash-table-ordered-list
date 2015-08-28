'''
Created on 2 Jun 2015

@author: sl0
'''

from domain.entity import Song
from utils.ordered_list import OrderedList


class Controller(object):
    
    def __init__(self, repo):
        self._repo = repo
        
    def get_all(self, comp):
        return self._repo.get_all(comp)
    
    def add_song(self, artist, song_name):
        song = Song(artist, song_name)
        llist = self.get_all(lambda x, y: x<y)
        if llist is None:
            llist = OrderedList()
        if llist.find(song) == True:
            raise ValueError("Song is already in list!")
        llist.insert(song)
        self._repo.save_all(llist)
        return song
    
    def delete_song(self, artist, song_name):
        song = Song(artist, song_name)
        llist = self.get_all(lambda x, y: x<y)
        if llist.find(song) == False:
            raise ValueError("Song is not in list!")
        
        llist.erase(song)
        self._repo.save_all(llist)
        return song
    
    def rate_song(self,artist, song_name, rating):
        song = Song(artist, song_name)
        llist = self.get_all(lambda x, y: x<y)
        if llist.find(song) == False:
            raise ValueError("Song not in list!")
        song = llist.element(llist.position(song))
        song.rate(rating)
        llist.erase(song)
        llist.insert(song)
        self._repo.save_all(llist)
        return song    
