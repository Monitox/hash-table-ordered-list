'''
Created on 2 Jun 2015

@author: sl0
'''

class UI:
    
    def __init__(self, ctrl):
        self._ctrl = ctrl
        
    def _print_menu(self):
        print("         1. Show all songs\n \
        2. Add song\n \
        3. Delete song\n \
        4. Rate song!\n \
        5. Exit")
    
    def _show_all(self):
        llist = self._ctrl.get_all(lambda a, b: a.rating < b.rating)
        for s in llist:
            print(str(s))
    
    def _add_song(self):
        artist = str(input("Enter the artist: "))
        song_name = str(input("Song name: "))
        song = self._ctrl.add_song(artist, song_name)
        print("Song "+str(song)+" added!")
        
    def _delete_song(self):
        artist = str(input("Enter the artist: "))
        song_name = str(input("Song name: "))
        song = self._ctrl.delete_song(artist, song_name)
        print("Song "+song.name+" deleted!")
    
    def _rate_song(self):
        artist = str(input("Enter the artist: "))
        song_name = str(input("Song name: "))
        rating = float(input("Rating: "))
        song = self._ctrl.rate_song(artist, song_name, rating)
        print("Song "+str(song)+" rated !")
        
    def startUI(self):
        while True:
            self._print_menu()
            inp = str(input("input: "))
            try:
                if inp == "1":
                    self._show_all()
                if inp == "2":
                    self._add_song()
                if inp == "3":
                    self._delete_song()
                if inp == "4":
                    self._rate_song()
                if inp == "5":
                    exit()
            except ValueError as msg:
                print(msg)