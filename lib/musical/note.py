import random

import config.musical
from lib.musical.utils import notation_to_midi, midi_to_notation


class Note:

    def __init__(self, beats, pitch=None, midipitch=None, velocity=64):
        if pitch != None:
            self.pitch = notation_to_midi(pitch)
        elif midipitch != None:
            self.pitch = midipitch
        else:
            raise ValueError("Neither pitch nor midipitch given!")

        self.beats = beats
        self.velocity = velocity

    def ticks(self):
        return int(round(self.beats * config.musical.TICKS_PER_BEAT))

    def __repr__(self):
        return midi_to_notation(self.pitch) + "/" + str(self.beats)

    @staticmethod
    def get_random():
        highest_pitch = notation_to_midi(config.musical.HIGHEST_NOTE)
        lowest_pitch = notation_to_midi(config.musical.LOWEST_NOTE)

        return Note(beats=random.choice(config.musical.NOTE_TIMES),
                    midipitch=random.randrange(lowest_pitch, highest_pitch),
                    velocity=random.randint(config.musical.MIN_VELOCITY, config.musical.MAX_VELOCITY))




