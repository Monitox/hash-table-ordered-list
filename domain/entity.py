'''
Created on 30 May 2015

@author: sl0
'''

class Song:
    def __init__(self, artist, song_name, rating=5.0, number_of_ratings=0):
        artist = artist.strip()
        song_name = song_name.strip()
        self._name = (artist + ";;" + song_name).upper()
        self._rating = rating
        self._number_of_ratings = number_of_ratings
    
    def __str__(self):
        return self.name + " " + str(self.rating)
    
    def __eq__(self, other):
        if(other is not None):
            return self.name == other.name
        return False
    
    def __lt__(self, other):
        return self.rating < other.rating

    def __le__(self, other):
        return self.rating <= other.rating
    
    def __gt__(self, other):
        return self.rating > other.rating
    
    def __ge__(self, other):
        return self.rating >= other.rating
    
    def get_name(self):
        name = self._name.replace(";;", " - ")
        return name
    
    def get_key(self):
        return self._name

    def get_rating(self):
        return self._rating

    def get_number_of_ratings(self):
        return self._number_of_ratings

    def set_rating(self, value):
        self._grade = value
    
    def rate(self, rating):
        median = self.rating * (self._number_of_ratings) + rating
        self._number_of_ratings += 1
        median /= self._number_of_ratings
        # pentru a obtine doar o zecimala
        self._rating = int((median * 10) + 0.5) / 10.0

    name = property(get_name, None, None, None)
    rating = property(get_rating, set_rating, None, None)
    number_of_ratings = property(get_number_of_ratings, None, None, None)

