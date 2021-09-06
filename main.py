from playsound import playsound as pys

class play_sound:

    def input_char(self, input_char):
        ret_char = list(input_char)
        return ret_char

    def read_sound(self):
        for i in self.input_char():
            name = "sound/" + i + ".mp3"
            pys(name)

class read_sound():
    def input_sound(self):
        input_sound = input('')

play = play_sound()
