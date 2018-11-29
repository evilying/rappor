import pandas as pd
import numpy as np
from utility import decode_rappor
import matplotlib.pyplot as pl

pl.rcParams.update({'font.size': 24})

data_dir = './results/'
filename = data_dir + 'hashes-result.csv'
data = pd.read_csv(filename)

pl.figure(figsize=(12, 7))
ind = [2, 4, 6, 8, 10, 12, 16]
pl.errorbar(ind, data['Mean_precision'], yerr=data['Std_precision'], fmt='-o')
pl.xticks(ind)
pl.errorbar(ind, data['Mean_recall'], yerr=data['Std_recall'], fmt='-x')
pl.ylim(0.3, 1)
pl.grid(b=None, which='major', axis='both')
pl.legend(['precision', 'recall'])
pl.title('precision-recall vs. hash functions #')
pl.xlabel('hash function #')
pl.ylabel('ratio')
pl.savefig(data_dir + 'hashes.eps', format='eps', dpi=1000)
pl.show()
