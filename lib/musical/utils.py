import re

NOTES = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "bes", "b"]

def notation_to_midi(pitch):
    components = re.findall(r"[^\W\d_]+|\d+", pitch.lower())
    note = NOTES.index(components[0])
    octave = int(components[1])

    return octave*12 + note


def midi_to_notation(pitch):
    octave = pitch // 12
    note = pitch % 12

    return NOTES[note]+ str(octave)