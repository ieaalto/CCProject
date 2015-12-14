import config.musical
from config.musical import *
from lib.musical.feature_utils import *
from lib.musical.utils import notation_to_midi


@feature(notation_to_midi(LOWEST_NOTE), notation_to_midi(HIGHEST_NOTE))
def mean_pitch(genotype, i):
    return genotype[i].pitch

@feature(MIN_VELOCITY, MAX_VELOCITY)
def mean_velocity(genotype, i):
    return genotype[i].velocity

@feature(NOTE_TIMES[0], NOTE_TIMES[-1])
def note_time(genotype, i):
    return genotype[i].beats

@feature(0,127)
def pitch_variance(genotype, i):
    start = max(0, i - REGION_RADIUS)
    end = min(len(genotype), i + REGION_RADIUS + 1)
    mn, mx = None, None
    for j in range(start, end):
        if mn == None or genotype[j].pitch < mn:
            mn = genotype[j].pitch
        if mx == None or genotype[j].pitch > mx:
            mx = genotype[j].pitch

    return mx-mn



