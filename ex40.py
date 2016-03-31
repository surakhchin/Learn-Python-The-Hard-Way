class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self,):
        for line in self.lyrics:
            print line

print ("-" *20)


bridge = (["Sometimes I feel like",
          "I don't have a partner",
          "Sometimes I feel like",
          "My only friend",
          "Is the city I live in",
          "The city of Angles!"])

eminem = (["I'm slim shady",
           "Yes I'm the real shady",
           "Will the real slim shday",
           "Please stand up?"])

any_song = Song(bridge)


any_song.sing_me_a_song()

any_song1 = Song(eminem)

any_song1.sing_me_a_song()



