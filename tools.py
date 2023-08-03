import fiona
import geopandas as gpd

class generador():
    def __init__(self):
        super().__init__()
    
    def puntos(self,data,ruta,nombre,sis_coor):
        esquema={'geometry':'Point','properties':[('Name','str')]}
        shape=fiona.open(ruta+"/"+nombre+".shp", mode='w', driver='ESRI Shapefile',schema = esquema, crs = sis_coor)
        for _, row in data.iterrows():
            punto_propiedad={
                'geometry' : {'type':'Point',
                            'coordinates': (float(row.x),float(row.y))},
                'properties': {'Name' : row.id},
            }
            shape.write(punto_propiedad)
        shape.close()
    
    def lineas(self,data,ruta,nombre,sis_coor):
        esquema={'geometry':'LineString','properties':[('Name','str')]}
        shape=fiona.open(ruta+"/"+nombre+".shp", mode='w', driver='ESRI Shapefile',schema = esquema, crs = sis_coor)
        lista_puntos=[]
        for _, row in data.iterrows():
            lista_puntos.append((row.x,row.y))
        sh_propiedad = {
        'geometry' : {'type':'LineString',
                        'coordinates': lista_puntos},
        'properties': {'Name' : nombre}, 
        }                                           
        shape.write(sh_propiedad)
        shape.close()

    def poligono(self,data,ruta,nombre,sis_coor):
        esquema = {
        'geometry':'Polygon',
        'properties':[('Name','str')]
        }
        shape=fiona.open(ruta+"/"+nombre+".shp", mode='w', driver='ESRI Shapefile',schema = esquema, crs = sis_coor)
        lista_puntos = []
        for _, row in data.iterrows():
            lista_puntos.append((float(row.x),float(row.y)))
        lista_puntos.append(lista_puntos[0])
        shp_propiedad = {
        'geometry' : {'type':'Polygon',
                        'coordinates': [lista_puntos]},
        'properties': {'Name' : nombre},
        }                                       
        shape.write(shp_propiedad)
        shape.close()
    
    def crear_KML(self,ruta,tipo,nombre):
        if tipo==0:
            shp=gpd.read_file(ruta+"/"+nombre+".shp")
            gpd.io.file.fiona.drvsupport.supported_drivers['KML']='rw'
            ruta=ruta.split("/")
            if len(ruta)>1:ruta.pop(-1)
            ruta="/".join(ruta)
            shp.to_file(ruta+"/"+nombre+".kml",driver="KML")
        else:
            shp=gpd.read_file(ruta+"/"+nombre+".shp")
            gpd.io.file.fiona.drvsupport.supported_drivers['KML']='rw'
            shp.to_file(ruta+"/"+nombre+".kml",driver="KML")

    def crear_linea_puntos(self,ruta,ruta2,nombre):
        kml1=open(ruta+"/linea.kml","r").readlines() 
        kml2=open(ruta+"/puntos.kml","r").readlines() 
        nuevo=open(ruta2+"/"+nombre+".kml","w") 
        for i in kml1[:-1]: 
            nuevo.write(i) 
        for i in kml2[3:]: 
            nuevo.write(i) 
        nuevo.close()    

