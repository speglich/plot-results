from ssl import CertificateError
import pandas as pd
from matplotlib import pyplot as plt

# Arrumar titulo na posição Certa 
# Colocar em segundos


df_naive = pd.read_csv('naive.csv')
df_naive = df_naive.sort_values(by='N_CKP')
df_naive['experiment'] = df_naive.apply(lambda row: "DA - CKPs %d"%(row['N_CKP']), axis=1)
df_naive = df_naive.set_index('experiment')
df_naive = df_naive.filter(regex='timing')
df_naive = df_naive.div(1000).round(3)


df_cupy = pd.read_csv('cupy.csv')
df_cupy = df_cupy.sort_values(by='N_CKP')
df_cupy['experiment'] = df_cupy.apply(lambda row: "UMA - CKPs %d"%(row['N_CKP']), axis=1)
df_cupy = df_cupy.set_index('experiment')
df_cupy = df_cupy.filter(regex='timing')
df_cupy = df_cupy.div(1000).round(3)

df_external = pd.read_csv('external_allocator.csv')
df_external = df_external.sort_values(by='N_CKP')
df_external['experiment'] = df_external.apply(lambda row: "EA - CKPs %d"%(row['N_CKP']), axis=1)
df_external = df_external.set_index('experiment')
df_external = df_external.filter(regex='timing')
df_external = df_external.div(1000).round(3)

df = pd.concat([df_naive, df_cupy, df_external], axis=0)

ax = df.plot(kind='bar',stacked=True)

title = 'Execution Time Default Allocator (DA) x Unified Memory Allocator (UMA) x External Allocator (EA)'


ax.set_ylabel('Time [s]')
ax.set_xlabel('Experiments per Number of Checkpoints')
ax.set_title(title)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('figures/results.png', dpi=350, bbox_inches='tight')
# print(keys)
