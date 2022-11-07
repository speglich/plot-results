from ssl import CertificateError
import pandas as pd
from matplotlib import pyplot as plt

# Arrumar titulo na posição Certa 
# Colocar em segundos

for nckp in [2, 4, 8, 16, 32, 64, 128]:
    df_ckp = pd.read_csv(f'ckp{nckp}.csv')
    df_ckp = df_ckp.sort_values(by='BLK')
    df_ckp['experiment'] = df_ckp.apply(lambda row: "%d"%(row['BLK']), axis=1)
    df_ckp = df_ckp.set_index('experiment')
    df_ckp = df_ckp.filter(regex='timing')
    df_ckp = df_ckp[df_ckp.columns.drop(list(df_ckp.filter(regex='storage')))]
    df_ckp = df_ckp.div(1000).round(3)

    df = pd.concat([df_ckp], axis=0)

    ax = df.plot(kind='bar',stacked=True)

    title = f'Execution Time [s] per Block Size - {nckp} Checkpoints - CPU'

    ax.set_xticklabels(df.index,rotation=0)
    ax.set_ylabel('Time [s]')
    ax.set_xlabel('Block Size')
    ax.set_title(title)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(f'figures/blk-checkpoint{nckp}.png', dpi=350, bbox_inches='tight')
# print(keys)
