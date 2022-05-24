###                        Gráfico de Linhas                      ###
### Quantidade de artistas no top 100 por data, decorrer dos anos ###
##                      Importar bibliotecas                       ##
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap3 import wrap
import re

##                         Importar dados                          ##
#https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019
spotify = pd.read_csv(r'C:\Users\Bárbara\OneDrive\Documentos\estudos\kaggle\spotify\Spotify top 100.csv')
plt.figure(figsize=(15, 6),facecolor = '#030926')

##                              Título                             ##
title = plt.title('Artistas no Top 100 - Ano-Mês')
plt.setp(title, color='w')

##                               Eixo                              ##
ax = plt.gca()
ax.xaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.patch.set_facecolor('#030926')

##                       Tratamento dos dados                      ##
qtd_year = spotify.groupby(['top year'])['artist'].nunique()
qtd_year.sort_index().plot(color = '#3DFEFB', marker = 'D')
ym =spotify.groupby(['top year'])['top year'].unique()
#ym =spotify['top year'].unique()
cont = qtd_year.count()
print(cont)

##                        Exibição do gráfico                      ##
plt.show()
