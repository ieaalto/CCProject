import config.musical
from config.musical import MIN_VELOCITY, MAX_VELOCITY, LOWEST_NOTE, HIGHEST_NOTE
from lib.musical.feature_utils import *
from lib.musical.utils import notation_to_midi


@normalize(notation_to_midi(LOWEST_NOTE), notation_to_midi(HIGHEST_NOTE))
def mean_pitch(genotype, i):
    return genotype[i].pitch

@normalize(MIN_VELOCITY, MAX_VELOCITY)
def mean_velocity(genotype, i):
    return genotype[i].velocity

def mean_note_length(target):
    max_diff = max([math.fabs(time - target) for time in config.musical.NOTE_TIMES])

    @normalize(0, max_diff)
    def note_len(genotype, i):
        return math.fabs(genotype[i].beats - target)

    return note_len

