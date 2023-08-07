#--------------librerias --------------
import tkinter
import customtkinter
from tkinter import filedialog
from PIL import Image
import pandas as pd
import os
import shutil
from tools import *
from windows import *
#--------------------------------------

#---------- inicio ventana
customtkinter.set_appearance_mode("System")    #modo de apariencia del sistema
customtkinter.set_default_color_theme("blue")  #establece el color de la app en azul 

#------------- Clase App ------------------

class App(customtkinter.CTk):
    """
    Clase encargada de la ventana principal y la interacción con los botones.
    al ser invocada inicia con customtkinter.CTK -> generando la ventana principal.
    """

    ruta_arch=""
    paso1="1. Las coordenadas deben estar almacenadas en un archivo .xlsx o .csv"
    paso2="2. El archivo debe tener 3 columnas y la primera fila debe llevar 3 campos (id x y)"
    paso3="ejemplo: (tambien puede descargar el archivo en el cuadro derecho)"
    paso4="3. Cargue el archivo"
    paso5="4. seleccione el tipo de 'geometria'"
    paso6="5. seleccione el sistema de coordenadas"
    paso7="6. seleccione el tipo de archivo a generar"
    nombre_arch=""
    carpeta_raiz=os.path.dirname(__file__)          #guarda la ruta donde se encuentra este archivo .py
    carpeta_img=os.path.join(carpeta_raiz,"img")    #crea la ruta relativa a la carpeta /img - la cual se guarda en la misma ruta del archivo .py

    def __init__(self):
        super().__init__()
        self.title("Crear shape's - kml")                                   #titulo de la ventana
        self.geometry(f"{1366}x{730}")                                      #tamaño de la ventana
        self.minsize(1300,650)                                              #tamaño minimo posible                     
        self.maxsize(1400,800)                                              #tamaño maximo posible
        self.state("zoomed")                                                #pantalla grande  
        self.iconbitmap(os.path.join(App.carpeta_img,"icono.ico"))          #establece el icono de la app
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        #barra lateral
        self.barralateral=customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.barralateral.grid(row=0,column=0,rowspan=4,sticky="nsew")
        self.barralateral.grid_rowconfigure(4, weight=1)

        self.arriba=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"logo_isa.png")),size=(236,125))
        self.logo_barra=customtkinter.CTkLabel(self.barralateral, image = self.arriba,text="")
        self.logo_barra.grid(row=0,column=0,padx=10,pady=(20,0))
        self.titulo_lat= customtkinter.CTkLabel(self.barralateral, text="Gestión predial", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.titulo_lat.grid(row=2, column=0, pady=(20, 10))
        
        self.tituloapp=customtkinter.CTkLabel(self.barralateral, text="Generador de .shp - .kml",font=customtkinter.CTkFont(size=15,weight="bold"))
        self.tituloapp.grid(row=4,column=0, pady=(0, 0))
        
        self.titulo_version= customtkinter.CTkLabel(self.barralateral, text="Version 1.1.0 \n\n2023", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.titulo_version.grid(row=5, column=0, pady=(0,50))
        
        
        self.abajo_lat=customtkinter.CTkFrame(self.barralateral,width=120,corner_radius=0)
        self.abajo_lat.grid(row=6,rowspan=4,sticky="nsew")
        self.abajo_lat.grid_rowconfigure(4,weight=1)
        
        self.apariencia= customtkinter.CTkLabel(self.abajo_lat, text="Modo apariencia:", anchor="w")
        self.apariencia.grid(row=0, column=0, padx=60, pady=(10, 0))
        self.menu_apariencia= customtkinter.CTkOptionMenu(self.abajo_lat, values=["System", "Dark","Light" ],command=self.apparence)
        self.menu_apariencia.grid(row=1, column=0, padx=60, pady=(5, 10))

        self.btn1 = customtkinter.CTkButton(self.abajo_lat, text ="CERRAR", command = self.destroy,fg_color="red",hover_color="#A50000",font=customtkinter.CTkFont(weight="bold")).grid(row=2,column=0,sticky="ew",padx=60,pady=(20, 30))
        #----------------------------
        #instrucciones
        self.caja_instrucciones=customtkinter.CTkFrame(self,fg_color="transparent")
        self.caja_instrucciones.grid(row=0,column=1,sticky="nsw")

        self.caja1=customtkinter.CTkFrame(self.caja_instrucciones,fg_color="transparent")
        self.caja1.grid(row=0,column=0)
        
        self.intrucc=customtkinter.CTkLabel(self.caja1, text="Instrucciones:",font=customtkinter.CTkFont(size=20,weight="bold"))
        self.intrucc.grid(row=0,column=0,padx=20, pady=(40, 0),sticky="w")
        
        self.paso1=customtkinter.CTkLabel(self.caja1, text=App.paso1,font=customtkinter.CTkFont(size=17),anchor="w")
        self.paso1.grid(row=1,column=0,padx=40, pady=(20, 0),sticky="w")
        self.paso2=customtkinter.CTkLabel(self.caja1, text=App.paso2,font=customtkinter.CTkFont(size=17),anchor="w")
        self.paso2.grid(row=2,column=0,padx=40, pady=(0, 0),sticky="w")
        self.paso3=customtkinter.CTkLabel(self.caja1, text=App.paso3,font=customtkinter.CTkFont(size=17),anchor="w")
        self.paso3.grid(row=3,column=0,padx=60, pady=(0, 0),sticky="w")
        
        self.ejemplo=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"ejemplo.png")),size=(296,90))
        self.img_ejemplo=customtkinter.CTkLabel(self.caja1, image = self.ejemplo,text="")
        self.img_ejemplo.grid(row=4,column=0,padx=80,pady=(0,0),sticky="w")
        
        self.paso4=customtkinter.CTkLabel(self.caja1, text=App.paso4,font=customtkinter.CTkFont(size=17),anchor="w")
        self.paso4.grid(row=5,column=0,padx=40, pady=(0, 0),sticky="w")
        self.paso5=customtkinter.CTkLabel(self.caja1, text=App.paso5,font=customtkinter.CTkFont(size=17),anchor="w")
        self.paso5.grid(row=6,column=0,padx=40, pady=(0, 0),sticky="w")
        self.paso6=customtkinter.CTkLabel(self.caja1, text=App.paso6,font=customtkinter.CTkFont(size=17),anchor="w")
        self.paso6.grid(row=7,column=0,padx=40, pady=(0, 0),sticky="w")
        self.paso7=customtkinter.CTkLabel(self.caja1, text=App.paso7,font=customtkinter.CTkFont(size=17),anchor="w")
        self.paso7.grid(row=8,column=0,padx=40, pady=(0, 0),sticky="w")
        
        #descargar formato
        self.caja_formato=customtkinter.CTkFrame(self.caja_instrucciones)
        self.caja_formato.grid(row=0,column=2,sticky="nsew",padx=(0,60),pady=30)
        
        self.titfor=customtkinter.CTkLabel(self.caja_formato,text="Generar formato",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.titfor.grid(row=0,column=0, pady=35,sticky="nsew")
        
        self.iconoxcel=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"excel.png")),size=(83,78))
        self.iconoxcel=customtkinter.CTkLabel(self.caja_formato, image = self.iconoxcel,text="")
        self.iconoxcel.grid(row=1,column=0,pady=(0,10),sticky="nsew")
        
        self.texto1=customtkinter.CTkLabel(self.caja_formato, text="Click en el botón para indicar la\ncarpeta donde se guardará el formato",font=customtkinter.CTkFont(size=15),anchor="w")
        self.texto1.grid(row=2,column=0, padx=10,pady=(0, 30))
        
        self.generar_formato=customtkinter.CTkButton(self.caja_formato, text="Generar",command=self.generar_archivo,font=customtkinter.CTkFont(weight="bold"))
        self.generar_formato.grid(row=3,column=0,padx=25,sticky="nsew")
        
        #-----------------------------

        self.caja_archivo=customtkinter.CTkFrame(self)
        self.caja_archivo.grid(row=1,column=1)
        
        #cargar archivo
        self.caja_archivo2=customtkinter.CTkFrame(self.caja_archivo)
        self.caja_archivo2.grid(row=0,column=0,sticky="nsew",padx=30,pady=30)
        self.iconoarch=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"archivo.png")),size=(100,100))
        self.iconoarch=customtkinter.CTkLabel(self.caja_archivo2, image = self.iconoarch,text="")
        self.iconoarch.grid(row=0,column=0,pady=(30,10),sticky="nsew",padx=2)
        self.texto1=customtkinter.CTkLabel(self.caja_archivo2, text="Agrega el archivo\ncon las coordenadas",font=customtkinter.CTkFont(size=15,weight="bold"),anchor="w")
        self.texto1.grid(row=1,column=0, padx=10,pady=(10, 20),sticky="nsew")
        self.boton_carga=customtkinter.CTkButton(self.caja_archivo2,command=self.abrir_archivo,text="ABRIR",font=customtkinter.CTkFont(weight="bold"))
        self.boton_carga.grid(row=3,column=0,sticky="nsew",rowspan=2)
      
        #tipo
        self.caja_tipo=customtkinter.CTkFrame(self.caja_archivo)
        self.caja_tipo.grid(row=0,column=1,sticky="nsew",padx=0,pady=30)
        
        self.label_radio_group = customtkinter.CTkLabel(master=self.caja_tipo, text="Tipo de geometría:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=30, pady=(20,10), sticky="nsew")
        self.value=tkinter.IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.caja_tipo, variable=self.value, value=0,text="Puntos",font=customtkinter.CTkFont(weight="bold"),command=self.desbloqueo)
        self.radio_button_1.grid(row=1, column=2, pady=(0,10),padx=20,  sticky="nsew")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.caja_tipo, variable=self.value, value=1,text="Líneas",font=customtkinter.CTkFont(weight="bold"),command=self.desbloqueo)
        self.radio_button_2.grid(row=2, column=2, pady=10,padx=20,  sticky="nsew")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.caja_tipo, variable=self.value, value=2,text="Polígono",font=customtkinter.CTkFont(weight="bold"),command=self.desbloqueo)
        self.radio_button_3.grid(row=3, column=2, pady=10,padx=20,  sticky="nsew")
        self.radio_button_22 = customtkinter.CTkRadioButton(master=self.caja_tipo, variable=self.value, value=3,text="Línea + puntos",font=customtkinter.CTkFont(weight="bold"),command=self.bloqueo)
        self.radio_button_22.grid(row=4, column=2, pady=(10,20),padx=20, sticky="nsew")

        #sistema de coordenadas
        self.caja_opciones=customtkinter.CTkFrame(self.caja_archivo)
        self.caja_opciones.grid(row=0,column=3,sticky="nsew",pady=30,padx=(30,0))
        self.text_sis=customtkinter.CTkLabel(self.caja_opciones,text="Sistema de\ncoordenadas",font=customtkinter.CTkFont(weight="bold"))
        self.text_sis.grid(row=0,column=0,pady=(30,10),padx=30)
        self.sistema=tkinter.StringVar(value="Origen nacional")
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.caja_opciones, dynamic_resizing=False,values=["Origen nacional", "WGS84"],variable=self.sistema)
        self.optionmenu_1.grid(row=1, column=0,padx=20)
        self.text_nombre=customtkinter.CTkLabel(self.caja_opciones,text="Nombre de\nla figura",font=customtkinter.CTkFont(weight="bold"))
        self.text_nombre.grid(row=3,column=0,pady=(30,10))
        self.text_input=customtkinter.CTkEntry(self.caja_opciones, placeholder_text="figura")
        self.text_input.grid(row=4, column=0, columnspan=2, padx=5, sticky="nsew")

        #generar figura
        self.caja_generar=customtkinter.CTkFrame(self.caja_archivo,fg_color="transparent")
        self.caja_generar.grid(row=0,column=4,sticky="nsew",padx=30,pady=30)
        self.iconogen=customtkinter.CTkLabel(self.caja_generar, text="",font=customtkinter.CTkFont(weight="bold"))
        self.iconogen.grid(row=0,column=0,sticky="nsew",pady=10)
        self.btn_kml=customtkinter.CTkButton(self.caja_generar, text="Generar .KML",font=customtkinter.CTkFont(weight="bold"),command=lambda:self.generar(self.value,App.nombre_arch,0))
        self.btn_kml.grid(row=1,column=0,pady=10)
        self.btn_shp=customtkinter.CTkButton(self.caja_generar, text="Generar .shp",font=customtkinter.CTkFont(weight="bold"),command=lambda:self.generar(self.value,App.nombre_arch,1))
        self.btn_shp.grid(row=2,column=0,pady=10)
        self.btn_ambos=customtkinter.CTkButton(self.caja_generar, text="Generar ambos",font=customtkinter.CTkFont(weight="bold"),command=lambda:self.generar(self.value,App.nombre_arch,2))
        self.btn_ambos.grid(row=3,column=0,pady=10)

    #---------------------------------------------------
    #funciones interaccion botones

    def verificar(ruta,nombre,id):
        if ruta!="":
            ruta=ruta.split("/")
            if len(ruta)>1:
                ruta.pop(-1)
            ruta="/".join(ruta)
            lista_dir=os.listdir(ruta)
            if id==0:
                if nombre+".kml" in lista_dir:
                    return False
                else:
                    return True
            else:
                if "shape" not in lista_dir:
                    os.mkdir(ruta+"/shape")
                lista_arch=os.listdir(ruta+"/shape")
                if nombre+".shp" in lista_arch or nombre+".kml" in lista_arch:
                    return False
                else:
                    return True
        else:
            return False
                    
      

    def generar(self,geometria,ruta,id):
        geometria=geometria.get()
        self.ventana_secundaria=ventana_secundaria()
        self.generador=generador()
        nombre=self.text_input.get()
        sistema=self.sistema.get()
        sis_coor={"WGS84":"EPSG:4326","Origen nacional":"EPSG:9377"}
        if nombre=="":
            nombre="figura"

        if App.verificar(ruta,nombre,id):
            if ".xlsx" in ruta:
                data=pd.read_excel(ruta)
            else:
                data=pd.read_csv(ruta)

            ruta=ruta.split("/")
            if len(ruta)>1:
                ruta.pop(-1)
            ruta="/".join(ruta)

            if geometria==3:
                self.generador.crear_linea_puntos(data,ruta,nombre,sis_coor[sistema])    
                self.ventana_secundaria.creado_correcto(ruta,data,sistema,geometria)

            else:
                if id==1:
                    self.imgcheck=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"comprobado.png")),size=(30,30))
                    self.iconogen.configure(text="")
                    self.iconogen.configure(image=self.imgcheck)
                    self.generar_geometria(geometria,data,ruta+"/shape",nombre,sis_coor[sistema])
                    self.ventana_secundaria.creado_correcto(ruta+"/shape",data,sistema,geometria)
                    
                elif id==0 or id==2:
                    self.imgcheck=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"comprobado.png")),size=(30,30))
                    self.iconogen.configure(text="")
                    self.iconogen.configure(image=self.imgcheck)
                    self.ventana_secundaria.creado_correcto(ruta,data,sistema,geometria)
                    if id==2:
                        self.generar_geometria(geometria,data,ruta+"/shape",nombre,sis_coor[sistema])
                        self.generador.crear_KML(ruta+"/shape",1,nombre)
                    else:
                        os.makedirs(ruta+"/00000000carpetamomentanea")
                        self.generar_geometria(geometria,data,ruta+"/00000000carpetamomentanea",nombre,sis_coor[sistema])
                        self.generador.crear_KML(ruta+"/00000000carpetamomentanea",0,nombre)
                        shutil.rmtree(ruta+"/00000000carpetamomentanea")                                     
        else:
            ruta="/".join(ruta.split("/")[:-1])
            if ruta=="":
                self.ventana_secundaria.error_crear()
                self.imgcheck=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"cancelar.png")),size=(30,30))
                self.iconogen.configure(text="")
                self.iconogen.configure(image=self.imgcheck)
            elif id==0:
                self.ventana_secundaria.archivo_existe(ruta,nombre)
            else:
                self.ventana_secundaria.archivo_existe(ruta+"/shape",nombre)
        
    def generar_geometria(self,tip,data,ruta_carpeta,nombre,sis_coor):
        self.generador=generador()
        if tip==0:
            print("puntos")
            self.generador.puntos(data,ruta_carpeta,nombre,sis_coor)#crea puntos
        elif tip==1:
            print("lineas")
            self.generador.lineas(data,ruta_carpeta,nombre,sis_coor)#crear linea
        else:
            print("poligono")
            self.generador.poligono(data,ruta_carpeta,nombre,sis_coor)#crear poligono  

    def generar_archivo(self):
        datafr=pd.DataFrame()
        datafr["id"],datafr["x"],datafr["y"]=None,None,None
        filename = filedialog.askdirectory(
            parent=self,
            title="Examinar archivo"
        )
        App.ruta_arch=filename
        self.ventana_error=ventana_secundaria()
        if filename!="":
            directorio=os.listdir(filename)
            if "formato_coordenadas.xlsx" in directorio:
                self.ventana_error.precaucion_formato(filename)
            else:
                try:
                    datafr.to_excel(filename+"/formato_coordenadas.xlsx",sheet_name="Sheet_name_1",index=False)
                    self.ventana_error.correcto_formato(filename)
                except:
                    self.ventana_error.error_carpeta_formato()
        else:
            self.ventana_error.error_carpeta_formato()
            
    def abrir_archivo(self):
        filename = filedialog.askopenfilename(
            parent=self,
            title="Examinar archivo",
            filetypes=[("Archivos de Excel",("*.xlsx","*.csv"))]
        )
        lista_a=filename.split("/")
        
        
        if filename!="":
            self.x=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"image.png")),size=(100,100))
            App.nombre_arch=filename
            self.iconoarch.configure(image=self.x)
            self.texto1.configure(text=lista_a[-1])
            self.texto1.configure(text_color="green")
            self.texto1.configure(padx=10)
            self.iconogen.configure(text="Click para generar")
            self.iconogen.configure(image="")
            print(App.nombre_arch) 

    
    def bloqueo(self):
        self.btn_shp.configure(state="disabled")
        self.btn_ambos.configure(state="disabled")
    
    def desbloqueo(self):
        self.btn_shp.configure(state="normal")
        self.btn_ambos.configure(state="normal")

    def apparence(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()