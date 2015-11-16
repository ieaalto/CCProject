import re

class Note:

    def __init__(self, time, pitch=None, midipitch=None, velocity=64):
        if pitch:
            self.pitch = _pitch_to_midi(pitch)
        elif midipitch:
            self.pitch = midipitch
        else:
            raise ValueError("Neither pitch nor midipitch given!")

        self.time = time
        self.velocity = velocity

    def __str__(self):
        return _midipitch_to_notation(self.pitch) + "/" + str(self.time)

class Bar:

    def __init__(self, notes = None):
        self.notes = []
        self.remaining = 1.0
        if notes:
            self.add_notes(notes)

    def add_note(self, note):
        if self.remaining - note.time < 0:
            return False
        self.notes.append(note)
        self.remaining -= note.time
        return True

    def add_notes(self, notes):
        for note in notes:
            if not self.add_note(note):
                raise ValueError("Notes won't fit!")

    def __str__(self):
        string = "["
        for note in self.notes:
            string += str(note) + ", "
        string = string[:len(string)-2] + "]"
        return string

class Song:

    def __init__(self, bars= None):
        self.bars = []
        if bars:
            self.bars = bars

    def notes(self):
        notes = []
        for bar in self.bars:
            for note in bar.notes:
                notes.append(note)

        return notes

def _pitch_to_midi(pitch):
    components = re.findall(r"[^\W\d_]+|\d+", pitch.lower())
    note = ["c", "cis", "d", "es", "e", "f", "fis", "g", "gis", "a", "bb", "b"].index(components[0])
    octave = int(components[1])

    return octave*12 + note

def _midipitch_to_notation(pitch):
    octave = pitch // 12
    note = pitch % 12

    return ["c", "cis", "d", "es", "e", "f", "fis", "g", "gis", "a", "bb", "b"][note]+ str(octave)

