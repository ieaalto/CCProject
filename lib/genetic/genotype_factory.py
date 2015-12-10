class GenotypeFactory:

    def __init__(self, Genotype, **kwargs):
        self.Genotype = Genotype
        self.params = kwargs

    def generate(self, n):
        return [self.Genotype(**self.params) for k in range(n)]
