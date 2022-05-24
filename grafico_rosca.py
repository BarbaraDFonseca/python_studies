###             Gráfico de rosca             ###
### Quantidade de artistas por tipo de grupo ###

##           importar bibliotecas             ##
from collections import Counter
from webbrowser import BackgroundBrowser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap3 import wrap
import re

##              importar dados                ##
#https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019
spotify = pd.read_csv(r'C:\Users\Bárbara\OneDrive\Documentos\estudos\kaggle\spotify\Spotify top 100.csv')
plt.figure(figsize=(6, 6),facecolor = '#030926')

##                  Título                    ##
title = plt.title('Tipos de Grupos')
plt.setp(title, color='w')

##            Tratamento dos dados            ##
qtd_artist = spotify.groupby(['artist type'])['artist'].count()
colors = ['#FC5649','#49FD95' , '#3DFEFB', '#247D49', '#6862FC']
qtd_artist.sort_index().plot(kind = 'pie', colors = colors, textprops={'color':"w"} )

##            Círculo para a rosca            ##
centre_circle = plt.Circle((0, 0), 0.55, fc='#030926')
fig = plt.gcf()

##            Exibição do gráfico             ##
fig.gca().add_artist(centre_circle)
plt.show()