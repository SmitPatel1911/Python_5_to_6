songs=["Arz Kiya Hai","Adhoora","Vaaroon Vaaroon"]

lc=lambda songs:songs.lower()

lower_songs=list(map(lc,songs))

print("Songs : ",lower_songs)
