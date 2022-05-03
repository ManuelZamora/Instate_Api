import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.colors import ListedColormap
import gmaps.geojson_geometries
from ipywidgets.embed import embed_minimal_html
from PIL import Image
from skimage import io
class mapa():
    

    def __init__(self, ubicaciones, corde):
        self.ubi=ubicaciones
        
        self.coordsCentrales=corde
        self.q=self.mapita()
        self.sts=""
        pass

    def mapita(self):
        gmaps.configure(api_key='AIzaSyCluVYulxQgv5nLTCroJhrqmIwdStl94aA')
        
        dfpricesZ = pd.DataFrame(self.ubi)
        print(dfpricesZ.head(0))
        dfpricesZ.describe()
        
         
        a=self.coordsCentrales
        lat = a.get('lat')
        lng = a.get('lng')

        figure_layout = {
            'width': '1361px',
            'height': '1000px',
            'border': '1px solid black',
            'padding': '1px'
        }

        fig = gmaps.figure(map_type="HYBRID", center = (lat, lng), zoom_level=14, layout = figure_layout)
        locations = dfpricesZ[['Latitude','Longitude']]
        weights = dfpricesZ['precio por ']

        hmLayer =  gmaps.heatmap_layer(locations, weights=weights, point_radius=180,opacity = 0.4)
        hmLayer.gradient = [(255,255,255,0.1),(0,0,255,0.6),(0, 255, 242,0.6),(0,255,0,0.6),(248, 255, 0,0.6),(255, 96, 0,0.6),(255,0,0,0.6)]
       
        fig.add_layer(hmLayer)
        #fig

        embed_minimal_html('export.html', views=[fig])
        fp = open('export.html', "r")

        content = fp.read()
        #st=str(content)
        self.sts=content
        return content
        fp.close() 
    def stss(self):
        return self.sts
    
    def imagen(self, ubi):
         fig, ax = plt.subplots(figsize=(7, 1))
         fig.subplots_adjust(bottom=0.5)

         cmap = mpl.cm.get_cmap('gist_rainbow_r')
         cmap = ListedColormap(cmap(np.linspace(0.25, 1, 256)))
         norm = mpl.colors.Normalize(vmin=495000.00, vmax=514000.00)
 

         fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
                    cax=ax, orientation='horizontal', label='precio por metro cuadrado')
         fig.savefig('colorbar.jpg')
 
class instanciamapa():
    def __init__(self, ubicaciones, corde):
        print("entro a instancia_houslist")
        self.hl= mapa(ubicaciones, corde)
        self.lista= self.hl.mapita()
        self.lista= self.hl.stss()
        print("ya hizo el csv")
        
    
    def listas(self):
        lista= self.hl.stss()
        return lista