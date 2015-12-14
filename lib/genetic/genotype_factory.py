class GenotypeFactory:
    '''
    Handles the creation of genotypes with given parameters.
    '''
    def __init__(self, Genotype, **kwargs):
        '''
        :param Genotype: a genotype class
        :param kwargs: the parameters passed to the new object upon instantiation.
        :return:
        '''
        self.Genotype = Genotype
        self.params = kwargs

    def generate(self, n):
        return [self.Genotype(**self.params) for k in range(n)]
