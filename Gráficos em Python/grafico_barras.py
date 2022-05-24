###                                     Gráfico de Barras                                    ###
### Quantidade de vezes que o artista foi o top do ano, os 10 que mais estiveram nesse pódio ###
##                                    Importar bibliotecas                                    ##
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap3 import wrap

##                                       Importar dados                                       ##
#https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019
spotify = pd.read_csv(r'C:\Users\Bárbara\OneDrive\Documentos\estudos\kaggle\spotify\Spotify top 100.csv')
plt.figure(figsize=(10, 6),facecolor = '#030926')

##                                            Título                                          ##
title = plt.title('Artistas Top Year ')
plt.setp(title, color='w')

##                                             Eixo                                           ##
ax = plt.axes()
ax.xaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.patch.set_facecolor('#030926')

##                                     Tratamento dos dados                                   ##
qtd_artist = spotify.groupby(['artist'])['top year'].count().sort_values(ascending=False)
qtd_artist.plot(kind='bar', color = '#49FD95', )
labels = qtd_artist.index.tolist()

##                                     Tratamento dos rótulos                                 ##
labels = ['\n'.join(wrap(l, 7)) for l in labels]
plt.xticks(range(len(labels)),labels, rotation=0)

##                                  Limite e exibição do gráfico                              ##
plt.xlim(-0.5,9.5) 
plt.show()
