class Song:

    def song_detail(self,title,artist,duration=0):
        self.title=title
        self.artist=artist
        self.duration=duration
    def show_details(self):
        print("Title : ",self.title)
        print("Artist : ",self.artist)
        print("Duration : ",self.duration)

s1=Song()
s2=Song()
s1.song_detail("Tera Naam Doon","Atif Aslam",263)
s2.song_detail("Aadat","Atif Aslam")
s1.show_details()
s2.show_details()
