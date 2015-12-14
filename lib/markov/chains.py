from lib.markov.markov import Markov
from lib.markov.lilypond_parser import parse
from config import settings

melody = Markov(order=settings.ORDER)
melody.learn(parse(open(settings.MARKOV_DATA).read()))

