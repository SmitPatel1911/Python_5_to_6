def get_unique_artists(p1,p2):
    return p1.union(p2)


p1={"Arijit Singh","Sachin-Jigar","Anuv Jain","Atif Aslam"}
p2={"Anuv Jain","Atif Aslam","Arijit Singh","Aditya Rikhari"}

unique_artists=get_unique_artists(p1,p2)

print("Unique Artists : ",unique_artists)
