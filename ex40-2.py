class Song(object):

    def __init__(self, lyrics): #this line stores instance variable in self
        self.lyrics = lyrics

    def sing_me_a_song(self): # this line takes the instance variable and uses it
        for line in self.lyrics:
            print line

bridge = (["Sometimes I feel like",
          "I don't have a partner",
          "Sometimes I feel like",
          "My only friend",
          "Is the city I live in",
          "The city of Angles!"])

under_the_bridge = Song(bridge)


yoyo = (["Uhh this is a test",
         "To see if I am dumb."])

under_the_bridge.sing_me_a_song()

xoxo = Song(yoyo)

xoxo.sing_me_a_song()





