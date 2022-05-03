import pandas as pd

#19.201244, -96.167428
#P.º Playa Linda 18, Buenavista, 91850 Veracruz, Ver.
class filtro():
    def __init__(self, archivo):
#tenemos que sacar la latitud y la langitud de cada direccion de csv
        archivofiltrado = archivo[:-4]
        print("nombre original", archivo)
        print("archivo filtrado",archivofiltrado)
        df = pd.read_csv(archivo)
 
        df = df[df['latitude'] < 19.201244+0.015]
        df = df[df['latitude'] > 19.201244-0.015]

        df = df[df['longitude'] < -96.167428+0.015]
        df = df[df['longitude'] > -96.167428-0.015]
        
        df.to_csv(archivofiltrado+'Filtrado.csv')
        print(df.head())