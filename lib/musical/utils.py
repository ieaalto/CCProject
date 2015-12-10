import re


def notation_to_midi(pitch):
    components = re.findall(r"[^\W\d_]+|\d+", pitch.lower())
    note = ["c", "cis", "d", "es", "e", "f", "fis", "g", "gis", "a", "bb", "b"].index(components[0])
    octave = int(components[1])

    return octave*12 + note


def midi_to_notation(pitch):
    octave = pitch // 12
    note = pitch % 12

    return ["c", "cis", "d", "es", "e", "f", "fis", "g", "gis", "a", "bb", "b"][note]+ str(octave)