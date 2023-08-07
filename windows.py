#--------------librerias --------------
import customtkinter
import os
from PIL import Image
from tkintermapview import TkinterMapView
from pyproj import Transformer
import numpy as np
#--------------------------------------

#-------------- Clase ventana_secundaria --------------

class ventana_secundaria(customtkinter.CTkToplevel):
    """
    Cuando se llama la clase, customtkinter.CTKToplevel genera una ventana secundaria vacía.
    los metodos contenidos en la clase se usan para llenar la ventana secundaria con la 
    información necesaria (icono, mensaje y boton)
    """

    carpeta_raiz=os.path.dirname(__file__)                 #guarda la ruta donde se encuentra este archivo .py
    carpeta_img=os.path.join(carpeta_raiz,"img")           #crea la ruta relativa a la carpeta /img - la cual se guarda en la misma ruta del archivo .py
    
    def __init__(self):
        super().__init__()
        self.grab_set()
        self.resizable(width=False, height=False)          #no permite cambiar el tamaño de la ventana
        self.iconbitmap(os.path.join(ventana_secundaria.carpeta_img,"icono.ico")) 

    def boton_cerrar_rojo(self,index=int):
        """
        boton_cerrar_rojo(index) -> crea un boton con el texto "CERRAR" en color rojo   
                                    recibe como parametro la posicion fila donde se ubicará
        """
        self.btn_cerrar = customtkinter.CTkButton(self, text ="CERRAR", command = self.destroy,fg_color="red",hover_color="#A50000")
        self.btn_cerrar.grid(row=index,column=0,sticky="ew",padx=60,pady=(20, 30))
    
    def boton_cerrar_verde(self,index=int):
        """
        boton_cerrar_verde(index) -> crea un boton con el texto "CERRAR" en color verde  
                                    recibe como parametro la posicion fila donde se ubicará
        """
        self.btn_cerrar = customtkinter.CTkButton(self, text ="CERRAR", command = self.destroy,fg_color="green",hover_color="#0DAF0A")
        self.btn_cerrar.grid(row=index,column=0,sticky="ew",padx=60,pady=(20, 30))
    
    def boton_cerrar_amarillo(self,index=int):
        """
        crea un boton con el texto "CERRAR" en color amarillo  
        recibe como parametro la posicion fila donde se ubicará
        """
        self.btn_cerrar = customtkinter.CTkButton(self, text ="CERRAR", command = self.destroy,fg_color="#D68910",hover_color="#7E5109")
        self.btn_cerrar.grid(row=index,column=0,sticky="ew",padx=60,pady=(20, 30))
    
    def icono(self,name=str):
        """
        crea el icono en la ventana de aviso 
        recibe como parametro el nombre del icono a mostrar
        """
        self.iconoerror=customtkinter.CTkImage(Image.open(os.path.join(ventana_secundaria.carpeta_img,name+".png")),size=(100,100))
        self.iconoerror=customtkinter.CTkLabel(self, image = self.iconoerror,text="")
        self.iconoerror.grid(row=0,column=0,pady=(20,20),sticky="nsew")
            
    def error_carpeta_formato(self):
        """
        rellena la ventana secundaria con la información necesaria 
        para indicar que hubo error generando el formato .xlsx
        """
        self.title("!!ERROR!!")
        self.icono("cancelar")
        self.texterror=customtkinter.CTkLabel(self,text="Error generando el formato",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.texterror.grid(row=1,column=0,padx=40,sticky="nsew")
        self.boton_cerrar_rojo(2)
    
    def correcto_formato(self,ruta=str):
        """
        rellena la ventana secundaria con la información necesaria para 
        indicar que hubo error generando el formato .xlsx .
        recibe como parametro la ruta donde se generó el formato
        """
        self.title("Correcto")
        self.icono("comprobado")
        self.textcorrecto=customtkinter.CTkLabel(self,text="Formato generado correctamente en",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textcorrecto.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=80,height=20)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)
        self.boton_cerrar_verde(3)
    
    def precaucion_formato(self,ruta=str):
        """
        rellena la ventana secundaria con la información necesaria para 
        indicar que ya existe el formato .xlsx .
        recibe como parametro la ruta donde se encuentra el formato
        """
        self.title("Precaucion")
        self.icono("precaucion")
        self.textp=customtkinter.CTkLabel(self,text="Formato ya existe en la carpeta",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textp.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=80,height=20)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)
        self.boton_cerrar_amarillo(3)
    
    def creado_correcto(self,ruta,data,sis_coor,geometria):
        """
        rellena la ventana secundaria con la información necesaria para 
        indicar que se genraron los archivos correctamente .
        recibe como parametro la ruta donde se guardaron los archivos
        """
        self.title("Correcto")
        self.icono("comprobado")
        self.textcorrecto=customtkinter.CTkLabel(self,text="Creado correctamente en",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textcorrecto.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=80,height=20)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)
        self.mapa(data,sis_coor,geometria)
        self.boton_cerrar_verde(4)
    
    def error_crear(self):
        """
        rellena la ventana secundaria con la información necesaria para 
        indicar que no el usuario no agregó el archivo Excel .
        """
        self.title("!!ERROR!!")
        self.icono("cancelar")
        self.texterror=customtkinter.CTkLabel(self,text="Debe cargar el archivo Excel",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.texterror.grid(row=1,column=0,padx=40,sticky="nsew")
        self.boton_cerrar_rojo(2)

    def archivo_existe(self,ruta,nombre):
        """
        rellena la ventana secundaria con la información necesaria para 
        indicar que se los archivos que se quieren generar ya existen con ese nombre .
        recibe como parametro la ruta donde se encuentran los archivos 
        y el nombre de los archivos
        """
        self.title("!!ERROR!!")
        self.icono("precaucion")
        self.textp=customtkinter.CTkLabel(self,text="Archivo con el nombre '"+nombre+"' ya existe en la carpeta",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textp.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=80,height=20)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)
        self.boton_cerrar_amarillo(3)
    
    def mapa(self,data,sis_coor,geometria):
        zona_mapa=customtkinter.CTkFrame(self)
        zona_mapa.grid(row=3, column=0, pady=(20,0), padx=20, sticky="nsew")
        mapa_satelite = TkinterMapView(zona_mapa, corner_radius=0,width=800, height=500)
        mapa_satelite.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=18)
        #mapa_satelite.set_address("medellin")
        mapa_satelite.grid(row=2, rowspan=4, column=1, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))
        lista=list(zip(data.x,data.y))
        if sis_coor=="Origen nacional":
            transformer = Transformer.from_crs('EPSG:9377','EPSG:4326',always_xy=True)
            lista = np.array(list(transformer.itransform(lista)))
            data['x']=lista[:,0]
            data['y']=lista[:,1]
        centro=lista[len(lista)//2]
        if geometria==0:  #puntos
            for _, row in data.iterrows():
                mapa_satelite.set_marker(row.y,row.x,text=row.id,text_color="white",marker_color_outside="#F2E205",marker_color_circle="#A69B03")
        elif geometria==1: #linea
            mapa_satelite.set_path(list(zip(data.y,data.x)),color="red",width=2)
        elif geometria==2: #poligono
            mapa_satelite.set_polygon(list(zip(data.y,data.x)),outline_color="red")
        else:              #punto + linea
            for _, row in data.iterrows():
                mapa_satelite.set_marker(row.y,row.x,text=row.id,text_color="white",marker_color_outside="#F2E205",marker_color_circle="#A69B03")
            mapa_satelite.set_path(list(zip(data.y,data.x)),color="red",width=2)
        mapa_satelite.set_position(centro[1],centro[0])
        mapa_satelite.set_zoom(15)
