import os
import glob
import pandas as pd

extension = 'csv'

results = {'ckp2' : 'results/ckp_2',
           'ckp4' : 'results/ckp_4',
           'ckp8' : 'results/ckp_8',
           'ckp16' : 'results/ckp_16',
           'ckp32' : 'results/ckp_32',
           'ckp64' : 'results/ckp_64',
           'ckp128' : 'results/ckp_128'}

for r in results:
    all_filenames = [i for i in glob.glob('{}/*.{}'.format(results[r], extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    combined_csv = combined_csv[combined_csv.columns.drop(list(combined_csv.filter(regex='count')))]
    combined_csv = combined_csv[combined_csv.columns.drop(list(combined_csv.filter(regex='N_CKP')))]
    combined_csv.to_csv('{}.csv'.format(r))