import itertools
import matplotlib.pyplot as plt
import seaborn as sns
from utils.io import load_yaml
from ast import literal_eval
sns.axes_style("white")


def show_training_progress(df, hue='model', metric='NDCG', name="epoch_vs_ndcg", save=True):
    fig, ax = plt.subplots(figsize=(8, 4))
    #plt.axhline(y=0.165, color='r', linestyle='-')
    ax = sns.lineplot(x='epoch', y=metric, hue=hue, style=hue, data=df)
    plt.tight_layout()
    if save:
        fig_path = load_yaml('config/global.yml', key='path')['figs']
        fig.savefig('{0}/train/progress/{1}.png'.format(fig_path, name),
                    bbox_inches="tight", pad_inches=0, format='png')
    else:
        plt.show()