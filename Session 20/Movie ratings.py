class Movie:
    def __init__(self,title,rating):
        self.title=title
        self._rating=0
        self.set_rating(rating)

    def get_rating(self):
        return self._rating

    def set_rating(self,rating):
        if 0<= rating <=10:
            self._rating=rating
        else:
            print("Error !!! Rating must be between 0 and 10 !!!")

movie=Movie("Inception",8.8)
print("Movie : ",movie.title)
print("Ratings : ",movie.get_rating())
movie.set_rating(9.2)
print("Updated Ratings : ",movie.get_rating())
movie.set_rating(12)
