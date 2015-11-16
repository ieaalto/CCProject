from lib.musical import model
import math

def save_midi(filename, song):

    notes = song.notes()
    bytes_hex = "4d54686400000006000000010060" #Midi headers
    bytes_hex += "4d54726b"+padded_hex(len(notes), 4)#Midi track chunk

    for note in notes:
        noteon = "90"+ padded_hex(note.pitch, 1)+padded_hex(note.velocity, 1)

    with open(filename, "wb") as f:
        f.write(bytearray.fromhex(bytes_hex))
        f.close()

def padded_hex(n, bytelength):
    string = hex(n)[2:]
    if len(string) > bytelength*2:
        raise ValueError("Number too big for "+bytelength+" bytes!")
    while len(string) < bytelength*2:
        string = "0"+string

    return string

