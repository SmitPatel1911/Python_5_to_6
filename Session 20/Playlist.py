class Playlist:

    def __init__(self):
        self._songs=[]

    def add_song(self,song):
        self._songs.append(song)

    def show(self):
        print("Playlist : ",self._songs)

s1=Playlist()
s1.add_song("Soulmate")
s1.add_song("Adhoora")
s1.add_song("Tu Chahiye")
s1.show()
