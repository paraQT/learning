class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
    "With pockets full of shells"])

lods_of_emone = Song(["Doin up the house is my bread and butter",
    "Me bird's page three and me car's a nutter",
    "Loadsamoney is the shout I utter",
    "As I wave my wad to the geezers in the gutter"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

lods_of_emone.sing_me_a_song()
