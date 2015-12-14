import sys

from lib import midi
from lib import vector_utils
from lib.data_representation.intervals import Intervals
from lib.genetic.algorithm import Genetic, truncation_selection
from lib.genetic.genotype_factory import GenotypeFactory
from lib.genetic.musical_genotype import MusicalGenotype
from lib.trends_service import fetch_trend_vector
from config import settings
import time

mock = "--mock" in sys.argv
search_term = input("Give a search term: ")

print("Fetching data...")
data = vector_utils.normalize(fetch_trend_vector(search_term, mock=mock))
intervals = Intervals(data)

start = time.clock()
print("Evolving...")

gen = Genetic(GenotypeFactory(MusicalGenotype, data={"test" : intervals},length=240), settings.POPULATION, settings.GENERATIONS, truncation_selection(0.5))

gen.evolve()

fittest = gen.get_n_fittest(1)[0]

print("Done in "+ str(time.clock() - start)+ "s")
print("Fitness of the fittest individual: "+ str(fittest.get_fitness()))

filename = (search_term+str(round(fittest.get_fitness(),9))).replace(" ", "_")

midi.save_midi(filename, fittest.notes)
print("Saved as " + filename + ".mid")

