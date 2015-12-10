import config.musical
from lib.musical.note import Note


class Notes:

    def __init__(self, notes):
        self.notes = notes
        self.duration = sum([n.beats for n in notes])

    def get_seqs(self, intervals):
        cut_points = [iv.relative_end()*self.duration for iv in intervals]
        seqs = []
        start, end, t, cp_i = 0, 0, 0, 0;

        for i in range(len(self.notes)):
            end = i+1
            t += self.notes[i].beats
            if t >= cut_points[cp_i]:
                cp_i += 1
                seqs.append( (start, end) )
                start = i+1

        return seqs


    def __getitem__(self, item):
        return self.notes[item]

    def __setitem__(self, key, value):
        self.duration -= self.notes[key].beats
        self.duration += value.beats
        self.notes[key] = value

    def __len__(self):
        return len(self.notes)

    def __repr__(self):
        return str(self.notes)

    @staticmethod
    def get_random(min_length):
        min_length = config.musical.TICKS_PER_BEAT * min_length
        dur = 0
        notes = []
        while dur < min_length:
            new = Note.get_random()
            dur += new.ticks()
            notes.append(new)

        return Notes(notes)