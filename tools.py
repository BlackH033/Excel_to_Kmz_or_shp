#--------------librerias --------------
import fiona
import geopandas as gpd
import os
import shutil
#--------------------------------------

#-------------- Clase generador() --------------
# continene los metodos necesarios para el procesamiento 

class generador():
    """
    La clase contiene los metodos encargados del procesamiento de la 
    información suministrada en el archivo Excel.
    """
    def __init__(self):
        super().__init__()
    
    # ---------- Metodo para generar Shapefile de tipo puntos -----------
    def puntos(self,data,ruta,nombre,sis_coor):
        """
        recibe 4 parametros: 
            1. data     -> DataFrame con la información de las coordenadas
                           el DataFrame lo crea pandas cuando se abre el archivo Excel
            2. ruta     -> La ruta donde se guardaran los archivos
            3. nombre   -> nombre que el usuario desea que lleve los archivos
            4. sis_coor -> el sistema de coordenadas en el cual están las coordenadas

        genera el shape de tipo punto (genera 5 archivos .shp,.cpg,.dbf,.prj,.shx) en la ruta especificada.
        """

        """
        esquema que llevará el shape, geometria de tipo punto y de propiedades un campo str llamado "id"
        """
        esquema={
            "geometry":"Point",
            "properties":[("id","str")]                
            }
        """
        fiona.open abre archivos, en este caso .shp
        fiona.open detecta que el archivo no existe y lo crea.
        se crea el shape vacío teniendo encuenta: 
            1. la ruta donde se guardará el archivo y el nombre dado por el usuario. 
               ruta+"/"+nombre+".shp" -> en la ruta se crea el achivo "nombre".shp
            2. se le idica que el archivo se abre en modo escritura  mode="w"
            3. se indica el diver, driver="ESRI Shapefile" indica que es formato shapefile
            4. el esquema creado en la variable anterior. indicando la estructura del shapefile
            5. el sistema de coordenadas en el cual se trabajará. 
               crs = sis_coor 
        """                          
        shape=fiona.open(
            ruta+"/"+nombre+".shp", 
            mode='w', driver="ESRI Shapefile",
            schema = esquema, 
            crs = sis_coor)
        """
        se usa un for para recorrer la información que genera data.iterrows().
        data.iterrows() -> devuelve un iterador del DataFrame "data" con dos objetos: un objeto con 
                           indices y un objeto con la informacion.
        "_" toma como valor cada objeto indice (esta información no se usa)
        "row" toma el valor del objeto con la información

        por cada iteración del for se creará un punto en el shape.
        para ello se crea el "esquema" que llevará cada punto, donde se indica la geometria la cual lleva:
            - el tipo de geometria ("type":"Point")
            - las coordenadas indicando coordenada X y coordenada Y ("coordinates": (row.x,row.y))
                como row es el objeto que almacena la información se extrae la información de "x" y "y" 
        además se agrega en el esquema la propiedad "id" y su valor ("properties:{"id":row.id})
        
        se usa .write para agregar el esquema al shape (shape.write(punto_esquema)  -> así en el shape se guarda cada punto)
        al finalizar el for se cierra el shape y ya queda el shape creado con todos los puntos que trae el DataFrame
        """
        for _, row in data.iterrows():                                       
            punto_esquema={                                                
                "geometry" : {"type":"Point",                               
                            "coordinates": (row.x,row.y)},                   
                "properties": {"id" : row.id},
            }
            shape.write(punto_esquema)
        shape.close()
    
    # ---------- Metodo para generar Shapefile de tipo linea -----------
    def lineas(self,data,ruta,nombre,sis_coor):
        """
        recibe 4 parametros: 
            1. data     -> DataFrame con la información de las coordenadas
                           el DataFrame lo crea pandas cuando se abre el archivo Excel
            2. ruta     -> La ruta donde se guardaran los archivos
            3. nombre   -> nombre que el usuario desea que lleve los archivos
            4. sis_coor -> el sistema de coordenadas en el cual están las coordenadas

        genera el shape de tipo linea (genera 5 archivos .shp,.cpg,.dbf,.prj,.shx) en la ruta especificada.
        """

        """
        esquema que llevará el shape, geometria de tipo linea y de propiedades un campo str llamado "id"
        """
        esquema={
            "geometry":"LineString",
            "properties":[("id","str")]
            }
        """
        fiona.open abre archivos, en este caso .shp
        fiona.open detecta que el archivo no existe y lo crea.
        se crea el shape vacío teniendo en cuenta: 
            1. la ruta donde se guardará el archivo y el nombre dado por el usuario. 
               ruta+"/"+nombre+".shp" -> en la ruta se crea el achivo "nombre".shp
            2. se le idica que el archivo se abre en modo escritura  mode="w"
            3. se indica el diver, driver="ESRI Shapefile" indica que es formato shapefile
            4. el esquema creado en la variable anterior. indicando la estructura del shapefile
            5. el sistema de coordenadas en el cual se trabajará. 
               crs = sis_coor 
        """ 
        shape=fiona.open(
            ruta+"/"+nombre+".shp", 
            mode="w", driver="ESRI Shapefile",
            schema = esquema, 
            crs = sis_coor
            )
        """
        se creea una lista vacía donde se almacenarán las coordenadas de cada punto conexión de linea.
        se usa un for para recorrer la información que genera data.iterrows().
        data.iterrows() -> devuelve un iterador del DataFrame "data" con dos objetos: un objeto con 
                           indices y un objeto con la informacion.
        "_" toma como valor cada objeto indice (esta información no se usa)
        "row" toma el valor del objeto con la información

        por cada iteración se guarda en la lista una tupla que contiene la coordenada "x" y "y" 
        de cada punto (lista_puntos.append((row.x,row.y)))
        como row es el objeto que almacena la información se extrae la información de "x" y "y"
        """
        lista_puntos=[]
        for _, row in data.iterrows():
            lista_puntos.append((row.x,row.y))
        """
        se crea el esquema de la linea indicando la geometria, la cual tiene:
            - el tipo de geomtria, que en este caso es linea ("type":"LineString")
            - las coordenadas, que están almacenadas en la lista "lista_puntos" ("coordinates": lista_puntos)
        además se agrega en el esquema la propiedad "id" y su valor ("properties:{"id":nombre})

        se usa .write para agregar el esquema al shape (shape.write(linea_esquema)
        se cierra el shape y ya queda el shape de linea creado con todos los puntos que trae el DataFrame
        """
        linea_esquema = {
        "geometry" : {"type":"LineString",
                        "coordinates": lista_puntos},
        "properties": {"id" : nombre}, 
        }                                           
        shape.write(linea_esquema)
        shape.close()

    # ---------- Metodo para generar Shapefile de tipo poligono -----------
    def poligono(self,data,ruta,nombre,sis_coor,opc):
        """
        recibe 5 parametros: 
            1. data     -> DataFrame con la información de las coordenadas
                           el DataFrame lo crea pandas cuando se abre el archivo Excel
            2. ruta     -> La ruta donde se guardaran los archivos
            3. nombre   -> nombre que el usuario desea que lleve los archivos
            4. sis_coor -> el sistema de coordenadas en el cual están las coordenadas
            5. opc      -> True o False para indicar si es multipoligono o no

        genera el shape de tipo poligono (genera 5 archivos .shp,.cpg,.dbf,.prj,.shx) en la ruta especificada.
        """

        """
        esquema que llevará el shape, geometria de tipo poligono y de propiedades un campo str llamado "id"
        """
        esquema = {
        "geometry":"Polygon",
        "properties":[("id","str")]
        }
        """
        fiona.open abre archivos, en este caso .shp
        fiona.open detecta que el archivo no existe y lo crea.
        se crea el shape vacío teniendo en cuenta: 
            1. la ruta donde se guardará el archivo y el nombre dado por el usuario. 
               ruta+"/"+nombre+".shp" -> en la ruta se crea el achivo "nombre".shp
            2. se le idica que el archivo se abre en modo escritura  mode="w"
            3. se indica el diver, driver="ESRI Shapefile" indica que es formato shapefile
            4. el esquema creado en la variable anterior. indicando la estructura del shapefile
            5. el sistema de coordenadas en el cual se trabajará. 
               crs = sis_coor 
        """ 
        shape=fiona.open(
            ruta+"/"+nombre+".shp", 
            mode="w", 
            driver="ESRI Shapefile",
            schema = esquema, 
            crs = sis_coor)
        """
        si opc tiene el valor de True:
            se genera una lista de un set que toma la columna id del DataFrame (se generan id sin repeticiones)
            se usa un for para recorrer la lista con los id unicos (i toma el valor de cada id - cada valor representa un poligono diferente)
            por cada valor de i (osea por cada poligono):
                se creea una lista vacía donde se almacenarán las coordenadas de cada vertice que conforma el poligono.
                se usa un for para recorrer la información que genera data.iterrows().
                data.iterrows() -> devuelve un iterador del DataFrame "data" con dos objetos: un objeto con 
                                indices y un objeto con la informacion.
                "_" toma como valor cada objeto indice (esta información no se usa)
                "row" toma el valor del objeto con la información
                si el id de la fila es igual al valor de i quiere decir que está en los vertices pertenecientes al poligono i
                se guarda en la lista una tupla que contiene la coordenada "x" y "y" de cada vertice (lista_vertice.append((row.x,row.y)))
                luego de que finalice el for, en lista_vertice se encuentran todas las coordendas de los vertices del poligono i

                luego se agrega el nombre y las coordenadas al esquema del shape perteneciente al poligono i (sh_propiedad)
                se agrega el esquema a al shape (shape.write())


        en caso de que opc tenga otro valor diferente a True:
            se creea una lista vacía donde se almacenarán las coordenadas de cada vertice que conforma el poligono.
            se usa un for para recorrer la información que genera data.iterrows().
            data.iterrows() -> devuelve un iterador del DataFrame "data" con dos objetos: un objeto con 
                            indices y un objeto con la informacion.
            "_" toma como valor cada objeto indice (esta información no se usa)
            "row" toma el valor del objeto con la información

            por cada iteración se guarda en la lista una tupla que contiene la coordenada "x" y "y" 
            de cada vertice (lista_vertice.append((row.x,row.y)))
            como row es el objeto que almacena la información se extrae la información de "x" y "y"
        """
        if opc==3:
            lista_id=list(set(data.id))
            for i in lista_id:
                lista_vertice = []
                for _, row in data.iterrows():
                    if row.id==i:
                        lista_vertice.append((float(row.x),float(row.y)))
                if lista_vertice[0]!=lista_vertice[-1]:
                    lista_vertice.append(lista_vertice[0])
                shp_propiedad = {
                "geometry" : {"type":"Polygon",
                                "coordinates": [lista_vertice]},
                "properties": {"id" : i},
                }                                       
                shape.write(shp_propiedad)
            shape.close()
        else:
            lista_vertice = []
            for _, row in data.iterrows():
                lista_vertice.append((float(row.x),float(row.y)))
            if lista_vertice[0]!=lista_vertice[-1]:
                    lista_vertice.append(lista_vertice[0])
            shp_propiedad = {
            "geometry" : {"type":"Polygon",
                            "coordinates": [lista_vertice]},
            "properties": {"id" : nombre},
            }                                       
            shape.write(shp_propiedad)
            shape.close()
    
    # ---------- Metodo para generar .kml -----------
    def crear_KML(self,ruta,tipo,nombre):
        """
        Este metodo recibe 3 parametros: 
            1. ruta -> la ruta en la cual se encuentran almacenados los .shp
            2. tipo -> este parametro puede ser 0 o 1.
                        0 quiere decir que el ususario elgió solo crear el .kml
                        1 quiere decir que el usuario eligió crear .kml y .shp
            3. nombre -> el nombre que el usuario elgió para nombrar el archivo

        - el tipo 0 trabaja desde una carpeta momentanea que se crea en main.py,
        - el tipo 1 trabaja sobre la misma carpeta donde se guardan los .shp
        """
        

        if tipo==0:            
            shp=gpd.read_file(ruta+"/"+nombre+".shp")                   #abre el archivo .shp creado en la carpeta que se encuentra en la ruta (que es una carpeta momentanea)    
            ruta=ruta.split("/")                                        #la ruta la toma como lista según los niveles lvl1/lvl2/lvl3 -> [lvl1,lvl2,lvl3]
            ruta.pop(-1)                                                # elimina un nivel, ya que no se quiere guardar en esa carpeta (esa carpeta es momentanea y se borrará)
            ruta="/".join(ruta)                                         # convierte a str la lista que contiene la ruta
            gpd.io.file.fiona.drvsupport.supported_drivers['KML']='rw'  #habilita el driver para leer archivos .kml
            shp.to_file(ruta+"/"+nombre+".kml",driver="KML")            # convierte el .shp en .kml con .to_file indicando el driver="KML" 
        
        elif tipo==1:
            shp=gpd.read_file(ruta+"/"+nombre+".shp")                   #abre el archivo .shp creado en la carpeta que se encuentra en la ruta (/shape)
            gpd.io.file.fiona.drvsupport.supported_drivers['KML']='rw'  #habilita el driver para leer archivos .kml
            shp.to_file(ruta+"/"+nombre+".kml",driver="KML")            #convierte el .shp a .kml y lo guarda en la misma carpeta

    # ---------- Metodo para generar .kml con linea y puntos a la vez -----------
    def crear_linea_puntos(self,data,ruta,nombre,sis_coor):
        """
        Este metodo recibe 4 parametros:
            1. data     -> DataFrame con la información de las coordenadas
                           el DataFrame lo crea pandas cuando se abre el archivo Excel
            2. ruta     -> la ruta donde se trabajará y guardaran archivos
            3. nombre   -> el nombre con el que el usuario quiere guardar el archivo
            4. sis_coor -> sistema de cooordenadas en el que están la información del DataFrame

        - se crea una carpeta momentanea pa almacenar archivos necesarios y luego la borra (la carpeta se llamará "00000000carpetamomentanea")
        para este metodo se parte de que un .kml es un archivo basado en XML. se usarán dos kml y se unirán.

        los .kml generados por la app siempre inician con 3 lineas
                <?xml version="1.0" encoding="utf-8" ?>
                <kml xmlns="http://www.opengis.net/kml/2.2">
                <Document id="root_doc">
        de resto son lineas con la información pertinente para la geometria.
        y cierran con la misma linea:
                </Document></kml>

        teniendo encuenta esto se toma el primer .kml sin tener encuenta la ultima linea (no se tiene encuenta la linea en posición -1 -> que es el cierre del archivo)
        seguido de eso se toma el segundo .kml y se toma apartir de la linea 4. esto con el fin de que no tome las 3 primeras linea mencionadas anteriormente.
        estas dos partes se unen en un solo documento .kml
        """
        self.generador=generador()
        os.makedirs(ruta+"/00000000carpetamomentanea")                                       #carpeta momentanea
        self.generador.puntos(data,ruta+"/00000000carpetamomentanea","puntos",sis_coor)      #crea un .shp de tipo punto con el nombre "puntos" en la carpeta momentanea
        self.generador.lineas(data,ruta+"/00000000carpetamomentanea","linea",sis_coor)       #crea un .shp de tipo linea con el nombre "linea" en la carpeta momentanea
        self.generador.crear_KML(ruta+"/00000000carpetamomentanea",1,"puntos")               #crea un .kml con el nombre "puntos" usando el .shp creado y que se encuentra en la carpeta momentanea
        self.generador.crear_KML(ruta+"/00000000carpetamomentanea",1,"linea")                #crea un .kml con el nombre "linea" usando el .shp creado y que se encuentra en la carpeta momentanea
        kml1=open(ruta+"/00000000carpetamomentanea"+"/linea.kml","r").readlines()            #abre el .kml creado con el nombre "linea" y se almacena en una lista
        kml2=open(ruta+"/00000000carpetamomentanea"+"/puntos.kml","r").readlines()           #abre el .kml creado con el nombre "puntos" y se almacena en una lista
        nuevo=open(ruta+"/"+nombre+".kml","w")                                               #se crea un nuevo archivo .kml con el nombre dado por el usuario
        for i in kml1[:-1]:                                                                  #se toma el primer .kml sin tener en cuenta la ultima linea
            nuevo.write(i)                                                                   #se agrega linea por linea al nuevo kml
        for i in kml2[3:]:                                                                   #se toma el segundo .kml sin tener encuenta las 3 primeras lineas
            nuevo.write(i)                                                                   #se agrega linea por linea al nuevo kml
        nuevo.close()                                                                        #se cierra el nuevo kml
        shutil.rmtree(ruta+"/00000000carpetamomentanea")                                     #se elimina la carpeta momentanea       
