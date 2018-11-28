import pandas as pd
from utility import decode_rappor

candidates = pd.read_csv('test.csv')
print('------')
client = candidates.sample(frac=0.8)

# client.to_csv('client.csv')
nbits = 16
icohort = 1
nhashes = 2
f = 0.1

decode_rappor(candidates, client, f, icohort, nbits, nhashes)
