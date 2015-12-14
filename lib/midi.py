import math
import re

import config.musical


def save_midi(filename, notes):

    bytes_hex = "4d546864"+ "00000006"+ "0000"+ "0001" + hex(config.musical.TICKS_PER_BEAT)[2:].zfill(4) #Midi headers

    notes_bytes = ""

    for note in notes:
        note_on, note_off = _note_on_and_off(note)
        notes_bytes += _variable_length_quantity(0) + note_on + _variable_length_quantity(note.ticks()) + note_off

    bytes_hex += "4d54726b"+ hex(len(notes_bytes)//2)[2:].zfill(8)+ notes_bytes + "ff2f00" #Midi track chunk

    filename = filename if re.match(r"^.+\.mid$", filename) else filename+".mid"
    with open(filename, "wb") as f:
        f.write(bytearray.fromhex(bytes_hex))
        f.close()

def _variable_length_quantity(n):
    b = bin(n)[2:]
    seven_bit_parts = [ b[max(i-7, 0):i] for i in range(len(b), 0,-7) ]
    binary = "0" + seven_bit_parts[0].zfill(7)

    for p in seven_bit_parts[1:]: binary = "1"+p.zfill(7) + binary

    h = hex(int(binary, 2))[2:]
    return h.zfill(math.ceil(len(h)/2)*2)

def _note_on_and_off(note):
    key_and_vel = hex(note.pitch)[2:].zfill(2) + hex(note.velocity)[2:].zfill(2)
    note_on = "90" + key_and_vel
    note_off = "80" + key_and_vel

    return note_on, note_off