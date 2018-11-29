import pandas as pd
import numpy as np
from utility import decode_rappor
import matplotlib.pyplot as pl

pl.rcParams.update({'font.size': 24})

data_dir = './results/'
filename = data_dir + 'cohort-result.csv'
data = pd.read_csv(filename)

pl.figure(figsize=(12, 7))
ind = [4, 8, 12, 16, 24, 32, 48, 64]
pl.errorbar(ind, data['Mean_precision'], yerr=data['Std_precision'], fmt='-o')
pl.xticks(ind)
pl.errorbar(ind, data['Mean_recall'], yerr=data['Std_recall'], fmt='-x')
pl.ylim(0.3, 1)
pl.grid(b=None, which='major', axis='both')
pl.legend(['precision', 'recall'])
pl.title('precision-recall vs. cohort number')
pl.xlabel('cohort number')
pl.ylabel('ratio')
pl.savefig(data_dir + 'cohort.eps', format='eps', dpi=1000)
pl.show()
