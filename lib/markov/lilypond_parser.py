from lib.musical.utils import NOTES


def parse(string):
    '''
    Parse a lilypond file for use with the Markov chain implementation and Notes.
    :param string:
    :return:
    '''
    notes = string.replace("\n", " ").split()
    base_oct = 5
    result = []

    for n in notes:
        if 'r' in n:
            continue

        oct = n.count("'") - n.count(",")

        n = "".join([a for a in list(n) if a.isalpha()])
        if n in NOTES:
            result.append(n+str(base_oct + oct))

    return result