import random

import config.musical
from lib.musical.utils import notation_to_midi, midi_to_notation
from lib.markov.chains import melody


class Note:
    '''
    Represents a single musical note.
    '''
    def __init__(self, beats, pitch=None, midipitch=None, velocity=64):
        '''
        :param beats: the duration of the note in beats.
        :param pitch: the pitch in notation. for example 'd6'. Specify either this or midipitch. Accepted note names are : c, cis, d, dis, e, f, fis, g, gis, a, bes, b
        :param midipitch: the pitch as a midi value.
        :param velocity: The velocity as a midi value.
        :return:
        '''
        if pitch != None:
            self.pitch = notation_to_midi(pitch)
        elif midipitch != None:
            self.pitch = midipitch
        else:
            raise ValueError("Neither pitch nor midipitch given!")

        self.beats = beats
        self.velocity = velocity

    def ticks(self):
        '''
        The duration of the note as a midi value.
        :return:
        '''
        return int(round(self.beats * config.musical.TICKS_PER_BEAT))

    def get_pitch_as_notation(self):
        '''
        Returns the pitch in notation, for instance 'd5'.
        :return:
        '''
        return midi_to_notation(self.pitch)

    def __repr__(self):
        return midi_to_notation(self.pitch) + "/" + str(self.beats)

    @staticmethod
    def get_random():
        return Note(beats=random.choice(config.musical.NOTE_TIMES),
                    pitch=melody.generate_one(),
                    velocity=random.randint(config.musical.MIN_VELOCITY, config.musical.MAX_VELOCITY))




