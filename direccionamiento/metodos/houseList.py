from numpy.core.numeric import NaN
from pandas.io.pytables import dropna_doc
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import os
import json
from datetime import date
from direccionamiento.metodos.csvFilter import filtro

from requests.api import delete

#C. Isla Montague 801-899, Villa California, 27085 Torreón, Coah.
#25.542243, -103.384470
#1.5 km = 0.015

class HouseList():

    def __init__(self, ubicacion):
        self.pagi=1
        self.ubicacion = ubicacion
        self.houseList = []
        self.url = ""
        self.NumPags = 0
        self.date =  date.today().strftime("%m_%d_%y")
        self.normalizeCityName()
        self.getNumPages()
        #self.setHouseList()
        if(self.pagi!=0):
            nombre =self.generateCsv()
            self.filtrado = self.lista() 
            self.ubicacion
       # filtro(nombre)


    def deleteSpacing(self, string):
        newString = string.split()
        newString = " ".join(newString)
        return newString

    def normalizeString(self, string):
        replacements = (
        ("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u"),('ñ','n'),
        ("Á","A"),("É","E"),("Í","I"),("Ó","O"),("Ú","U"),("Ñ","N")
        )
        for a, b in replacements:
            string = string.replace(a, b)
        return string

    def setHouseList(self):
        print('Getting data from: ' + self.url)

        for x in range(1, self.NumPags+1):
            pageNum = x
            header = {'User-Agent': 'Mozilla/5.0'}
            req = requests.get(self.normalizeString(self.url.format(self.ubicacion))+str(pageNum), headers=header)
            soup =  BeautifulSoup(req.content, 'html.parser')
            content = soup.find_all('div', class_='row ListingCell-row ListingCell-agent-redesign')
            for property in content:
                try:
                    titulo = self.normalizeString(property.find('h2', class_="ListingCell-KeyInfo-title").text).strip()
                    precio = property.find('span', class_="PriceSection-FirstPrice").text.strip()
                    nRecamaras = property.find('span', class_="KeyInformation-value_v2 KeyInformation-amenities-icon_v2 icon-bedrooms").text.strip()
                    m2_construidos = property.find('span', class_= "KeyInformation-value_v2 KeyInformation-amenities-icon_v2 icon-livingsize").text.replace('m²','').strip()
                    ubicacion = self.normalizeString(property.find('span', class_= "ListingCell-KeyInfo-address-text").text).strip()
                    link = property.find('div',class_='ListingCell-MainImage')
                    link = link.a['href']
                    image = property.find('div',class_="ListingCell-image")
                    imagen = image.img['data-src']

                except:
                    pass
                    #title =  NaN
                    precio =  NaN
                    nRecamaras = NaN
                    m2_construidos = NaN
                    ubicacion = NaN
                    link = NaN
                    imagen = NaN

                house = {
                    'titulo': titulo,
                    'precio': precio,
                    'nRecamaras': nRecamaras,
                    'm2_construidos': m2_construidos,
                    'ubicacion': ubicacion,
                    'link': link,
                    'imagen': imagen
                }
                self.houseList.append(house)
        sleep(2)
        print('Done')
        

    def getNumPages(self):
        header = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(self.normalizeString(self.url)+"1", headers=header)
        soup = BeautifulSoup(req.content, 'html.parser')
        content = soup.find_all('select',class_="sorting nativeDropdown js-pagination-dropdown")

        if content == None:
            print("No se encontro nada cerca de la zona")
            self.pagi=0

        else:
            print('Getting number of pages from:', self.url)
            for prop in content:
                pags = self.deleteSpacing(prop.find('option').text.strip())
                pags = pags.replace('Página 1 de ', '')
                print(pags)
            self.NumPags =  int(pags)
            self.setHouseList()
    
    

    def generateCsv(self):
        print('Creating csv file')
        #filename = 'CasasVenta_' + self.date + '_' + self.ubicacion + '_LAMU.csv'
        filenameNoNan = 'CasasVenta_' + self.date + '_' + self.ubicacion + '_NoNaN_LAMU.csv'
        dataFrame = pd.DataFrame(self.houseList)
        dataFrame.drop_duplicates(subset='link')
        dataFrameNoNaN = dataFrame.drop_duplicates(subset='link')
        #open(filename,'wb')
        #dataFrame.to_csv(filename)
        dataFrameNoNaN.dropna()
        dataFrameNoNaN= dataFrameNoNaN.dropna()
        print('.csv file created')
        return filenameNoNan
    
    def normalizeCityName(self):
        
        self.ubicacion =  self.normalizeString(self.ubicacion).lower()
        print(self.ubicacion)
        self.url = "https://www.lamudi.com.mx/casa/for-sale/{}/?page=".format(self.ubicacion)
        print(self.url)
    
    def lista(self):
        dataFrame = pd.DataFrame(self.houseList)
        dataFrame.drop_duplicates(subset='link')
        dataFrameNoNaN = dataFrame.drop_duplicates(subset='link')
        dataFrameNoNaN.dropna()
        dataFrameNoNaN= dataFrameNoNaN.dropna()

        df_ubicacion= dataFrameNoNaN
        ubicaciones= df_ubicacion['ubicacion']

        #print(ubicaciones)
        ubicaciones.groupby(level=0).head()
        ubibaciones= ubicaciones.groupby(level=0).head()
        ubicaciones.drop_duplicates()
        a=ubibaciones.drop_duplicates()
        auciliar=a.to_json(orient="split")
        folio=json.loads(auciliar)
        self.ubicacion=folio
        
        result = dataFrameNoNaN.to_json(orient="split") #al parecer aqui lo convierte en str
        parsed = json.loads(result)                     #aqui lo hace json
        json.dumps(parsed, indent=4)
        a= json.dumps(parsed, indent=4)
        
        return parsed
class instancia_houslist():
    def __init__(self, ubicacion):
        print("entro a instancia_houslist")
        self.hl= HouseList(ubicacion)
        self.lista= self.hl.filtrado
        self.ubicaion=self.hl.ubicacion
        print("ya hizo el csv")
        
    
    def listas(self):
        lista= self.hl.lista
        print(lista)
        return lista
    
#hl = HouseList('Tijuana')