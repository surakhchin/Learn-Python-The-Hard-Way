class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self, lyrics):
        for line in self.lyrics:
            print line

print ("-" *20)



under_the_bridge = Song(bridge)

bridge = (["Sometimes I feel like",
          "I dont have a partner",
          "Sometimes I feel like",
          "My only friend",
          "Is the city I live in",
          "The city of Angles!"])

under_the_bridge.sing_me_a_song(bridge)




