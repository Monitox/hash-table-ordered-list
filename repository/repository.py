'''
Created on 2 Jun 2015

@author: sl0
'''

from utils.ordered_list import OrderedList
from domain.entity import Song

class Repository():
    
    def __init__(self, txt):
        self._fn = txt
        
    def save_all(self, llist):
        f = open(self._fn, 'w')      
        for s in llist:
            f.write(s.get_key()+"//"+str(s.rating)+"//"+str(s.number_of_ratings)+"\n")
        f.close()
    
    def get_all(self, rel):
        f = open(self._fn, 'r', encoding = 'utf-8')
        llist = OrderedList(rel)
        for s in f:
            name, rating, number_of_ratings = s.split("//")
            rating = float(rating)
            number_of_ratings = int(number_of_ratings)
            artist, song_name = name.split(";;")
            artist.strip()
            song_name.strip()
            llist.insert(Song(artist, song_name, rating, number_of_ratings))
        f.close()
        return llist