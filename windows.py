import customtkinter
import os
from PIL import Image

class ventana_secundaria(customtkinter.CTkToplevel):
    carpeta_raiz=os.path.dirname(__file__)
    carpeta_img=os.path.join(carpeta_raiz,"img")
    
    def __init__(self):
        super().__init__()
        self.grab_set()
        self.resizable(width=False, height=False)
  
    def boton_cerrar_rojo(self,index=int):
        self.btn_cerrar = customtkinter.CTkButton(self, text ="CERRAR", command = self.destroy,fg_color="red",hover_color="#A50000")
        self.btn_cerrar.grid(row=index,column=0,sticky="ew",padx=60,pady=(20, 30))
    
    def boton_cerrar_verde(self,index=int):
        self.btn_cerrar = customtkinter.CTkButton(self, text ="CERRAR", command = self.destroy,fg_color="green",hover_color="#0DAF0A")
        self.btn_cerrar.grid(row=index,column=0,sticky="ew",padx=60,pady=(20, 30))
    
    def boton_cerrar_amarillo(self,index=int):
        self.btn_cerrar = customtkinter.CTkButton(self, text ="CERRAR", command = self.destroy,fg_color="#D68910",hover_color="#7E5109")
        self.btn_cerrar.grid(row=index,column=0,sticky="ew",padx=60,pady=(20, 30))
    
    def icono(self,name=str):
        self.iconoerror=customtkinter.CTkImage(Image.open(os.path.join(ventana_secundaria.carpeta_img,name+".png")),size=(100,100))
        self.iconoerror=customtkinter.CTkLabel(self, image = self.iconoerror,text="")
        self.iconoerror.grid(row=0,column=0,pady=(20,20),sticky="nsew")
            
    def error_carpeta_formato(self):
        self.title("!!ERROR!!")
        self.icono("cancelar")
        self.texterror=customtkinter.CTkLabel(self,text="Error generando el formato",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.texterror.grid(row=1,column=0,padx=40,sticky="nsew")
        self.boton_cerrar_rojo(2)
    
    def correcto_formato(self,ruta=str):
        self.title("Correcto")
        self.icono("comprobado")
        self.textcorrecto=customtkinter.CTkLabel(self,text="Formato generado correctamente en",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textcorrecto.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=80,height=20)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)
        self.boton_cerrar_verde(3)
    
    def precaucion_formato(self,ruta=str):
        self.title("Precaucion")
        self.icono("precaucion")
        self.textp=customtkinter.CTkLabel(self,text="Formato ya existe en la carpeta",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textp.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=80,height=20)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)
        self.boton_cerrar_amarillo(3)
   
    def error_seleccion(self):
        self.title("!!ERROR!!")
        self.icono("cancelar")
        self.texterror=customtkinter.CTkLabel(self,text="Seleccione un archivo",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.texterror.grid(row=1,column=0,padx=40,sticky="nsew")
        self.boton_cerrar_rojo(2)
    
    def creado_correcto(self,ruta):
        self.title("Correcto")
        self.icono("comprobado")
        self.textcorrecto=customtkinter.CTkLabel(self,text="Creado correctamente en",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textcorrecto.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=80,height=20)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)
        self.boton_cerrar_verde(3)
    
    def error_crear(self):
        self.title("!!ERROR!!")
        self.icono("cancelar")
        self.texterror=customtkinter.CTkLabel(self,text="Debe cargar el archivo Excel",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.texterror.grid(row=1,column=0,padx=40,sticky="nsew")
        self.boton_cerrar_rojo(2)

    def archivo_existe(self,ruta,nombre):
        self.title("!!ERROR!!")
        self.icono("precaucion")
        self.textp=customtkinter.CTkLabel(self,text="Archivo con el nombre '"+nombre+"' ya existe en la carpeta",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textp.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=80,height=20)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)
        self.boton_cerrar_amarillo(3)
