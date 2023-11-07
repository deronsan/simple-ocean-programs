from dwave.system import DWaveSampler, EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
Q = {(1, 1): -1, (1, 2): 1, (1, 3): 1, (2, 2): -1, (2, 4): 1, (3, 3): -1,(3, 4): 1, (4, 4): -1}
sampleset = sampler.sample_qubo(Q)
print(sampleset)
