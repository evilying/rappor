import pandas as pd
import numpy as np
from utility import decode_rappor
import matplotlib.pyplot as pl

result_dir = './results/'

filename = 'corpus_exper.csv'
candidates = pd.read_csv(filename).sample(frac=0.5, replace=True)

print(candidates.head())
print('------')

icohort = 1
nhashes = 2
f = 0.1
nbits = 64

client = candidates.sample(frac=0.8)

precision, acc = decode_rappor(candidates, client, \
    f, icohort, nbits, nhashes)
