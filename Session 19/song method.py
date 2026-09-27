class Song:

    def song_detail(self,title,artist,duration):
        self.title=title
        self.artist=artist
        self.duration=duration
    def show_details(self):
        print("Title : ",self.title)
        print("Artist : ",self.artist)
        print("Duration : ",self.duration)
    def song_preview(self):
        print(f"Playing 30 seconds preview of {self.title} by {self.artist}")
        
s1=Song()
s1.song_detail("Tera Naam Doon","Atif Aslam",263)
s1.show_details()
s1.song_preview()
