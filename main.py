from lib import midi
from lib import vector_utils
from lib.data_representation.intervals import Intervals
from lib.genetic.algorithm import Genetic, truncation_selection
from lib.genetic.genotype_factory import GenotypeFactory
from lib.genetic.musical_genotype import MusicalGenotype
from lib.musical.features import *
from lib.trends_service import fetch_trend_vector

data = vector_utils.normalize([0,1,2,3,4,5,6,5,4,3,2,1])

data = vector_utils.normalize(fetch_trend_vector("", mock=True))
intervals = Intervals(data)

gen = Genetic(GenotypeFactory(MusicalGenotype, data={"test" : intervals},length=240), 200, 20, truncation_selection(0.5))

gen.evolve()

fittest = gen.get_n_fittest(1)[0]

print([mean_velocity(fittest, i) for i in range(len(fittest))])

print(fittest.get_fitness())

midi.save_midi("evolved", fittest.notes)




