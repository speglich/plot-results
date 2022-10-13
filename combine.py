import os
import glob
import pandas as pd

extension = 'csv'

results = {'naive' : 'naive-checkpoint',
            'cupy' : 'cupy-checkpoint'}

for r in results:
    all_filenames = [i for i in glob.glob('{}/*.{}'.format(results[r], extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    combined_csv = combined_csv[combined_csv.columns.drop(list(combined_csv.filter(regex='count')))]
    combined_csv.to_csv('{}.csv'.format(r))