<!--
Creado por: Victor Daniel Rios Florez
 -->
![Generador de  kml o  shp](https://github.com/BlackH033/Excel_to_Kmz_or_shp/assets/95384317/416041f3-5225-4249-8ab6-9a4849749688)
<div align="center">
  <h3>
    Versión 1.1.0
  </h3>
</div>

---
![1 1](https://github.com/BlackH033/Excel_to_Kmz_or_shp/assets/95384317/09de5722-d2db-4b2d-a093-4d2c85a49bff)

---
Con esta app se pueden generar archivos .kml y/o .shp a partir de un archivo Excel (.xlsx o .csv). El archivo Excel debe de contner el id y las coordenadas del punto o vertice. La app puede generar las diferentes geometrias según la elección del usuario.

# 🧰 Funcionalidad
### V1.0.0
- [x] Puede generar formato en en .xlsx para agregar las coordenadas
- [x] Puede trabajar con archivos .xlsx o .csv
- [x] Puede generar puntos
- [x] Puede generar líneas
- [x] Puede generar polígono
- [x] Puede generar puntos combinados con lineas *(función solo habilitada para .kml)*
- [x] Puede trabajar coordenadas en Origen nacional o WGS84 (sistema de coordenas)
- [x] libertad para darle nombre a los archivos generados
- [x] Puede generar la información final en .kml
- [x] Puede generar la información final en .shp
- [x] Puede generar la información final en .kml y .shp a la vez (en un solo proceso)
### V1.1.0
- [x] En la ventana secundaria se muestra la geometria en mapa - Google Satelite

# ⚠️ Requerimientos
Se requieren de las siguientes librerias:
<br>

<div>
 <a href="https://pypi.org/project/customtkinter/" target="_blank">
  <img height=20 src="https://user-images.githubusercontent.com/95384317/258621438-3a0b7882-76d1-4d87-8bb2-5b97a9d54833.png"/>
  &nbsp;customtkinter
 </a>
</div>
<br>
<div>
 <a href="https://pypi.org/project/Fiona/" target="_blank">
  <img height=20 src="https://user-images.githubusercontent.com/95384317/258621438-3a0b7882-76d1-4d87-8bb2-5b97a9d54833.png"/>
  &nbsp;Fiona
 </a>
</div>
<br>
<div>
 <a href="https://pypi.org/project/geopandas/" target="_blank">
  <img height=20 src="https://user-images.githubusercontent.com/95384317/258621438-3a0b7882-76d1-4d87-8bb2-5b97a9d54833.png"/>
  &nbsp;geopandas
 </a>
</div>
<br>
<div>
 <a href="https://pypi.org/project/pandas/" target="_blank">
  <img height=20 src="https://user-images.githubusercontent.com/95384317/258621438-3a0b7882-76d1-4d87-8bb2-5b97a9d54833.png"/>
  &nbsp;pandas
 </a>
</div>
<br>
<div>
 <a href="https://pypi.org/project/Pillow/" target="_blank">
  <img height=20 src="https://user-images.githubusercontent.com/95384317/258621438-3a0b7882-76d1-4d87-8bb2-5b97a9d54833.png"/>
  &nbsp;Pillow
 </a>
</div>
<br>
<div>
 <a href="https://pypi.org/project/openpyxl/" target="_blank">
  <img height=20 src="https://user-images.githubusercontent.com/95384317/258621438-3a0b7882-76d1-4d87-8bb2-5b97a9d54833.png"/>
  &nbsp;openpyxl
 </a>
</div>
<br>
<div>
 <a href="https://pypi.org/project/tkintermapview/" target="_blank">
  <img height=20 src="https://user-images.githubusercontent.com/95384317/258621438-3a0b7882-76d1-4d87-8bb2-5b97a9d54833.png"/>
  &nbsp;tkintermapview
 </a>
</div>

# &nbsp;<img height=25 src="https://github.com/BlackH033/Excel_to_Kmz_or_shp/assets/95384317/cfef4e2b-2b84-497d-86f6-f60c142ecfc0"/> &nbsp;Configuración 

 1. Instala &nbsp;<a href="https://www.python.org/downloads/" target="_blank"><img height=20 src="https://user-images.githubusercontent.com/95384317/258619098-4284316f-437c-4ac5-8dc7-063121f4df9f.png"/></a>[Python 3.x](https://www.python.org/downloads/)
 2. Descarga o clona este repositorio
 3. Abre la carpeta del proyecto en tu IDE (VS code recomendado)
 4. Abre la carpeta desde la terminal (si usas VS code, la terminal ya se encuentra en la carpeta) y ejecuta lo siguiente:
    1. Crea un entorno virtual -> `py -m venv env`
    2. Activa el entorno victual creado -> `.\env\Scripts\activate`
    3. Instala las dependencias. se puede hacer de 2 maneras:
        1. Puedes instalar cada libreria -> `pip install nombrelibreria`
        2. O puedes usar el archivo *requirements.txt* -> `pip install -r requirements.txt` (esta opción es la recomendada)
 5. Reinicia el IDE
 6. Corre el script *main.py* desde el IDE o desde la terminal usando `./app.py` 

---

# 🖥️ Tutorial de uso

* *proximamente se agregará video*

---
# ⏬ Descarga la App
- [x] Dando click se puede descargar la App como un .exe portable
- [x] Este .exe no necesita de installaciones
- [x] Está listo para ser usado
  
 *Nota: la app fue creada haciendo uso de auto-py-to-exe que usa pyinstaller para generar el .exe apartir del script* -> <a href="https://pypi.org/project/auto-py-to-exe/" target="_blank"><img height=20 src="https://user-images.githubusercontent.com/95384317/258621438-3a0b7882-76d1-4d87-8bb2-5b97a9d54833.png"/></a>&nbsp;[auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/)

<!-- 
https://drive.google.com/uc?export=download&id=1WKARqlBHipikzmuTdzZL8XdTM4a_SZVi&name=Appv103.exe
-->
<div align="center">
  <a href="https://drive.google.com/uc?export=download&id=1WKARqlBHipikzmuTdzZL8XdTM4a_SZVi&name=Appv103.exe" target="_blank">
    <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/95384317/258607286-138a1990-c8d4-4543-9ead-0f7a29fd347a.png" width="300">
  </a>
</div>

---
<div align="center">
  
  <h3>
   <a href="https://github.com/BlackH033" target="_blank">
   Victor Rios 
   </a>
  <h3/>
 
  <a href="https://www.instagram.com/the_snake_rios/" target="_blank">
   <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/95384317/258623806-9b843046-68b2-4d0c-b060-3651ebd9adee.png" width="30">
  </a>&emsp;
 <a href="mailto:vdriosf@unal.edu.co" target="_blank">
   <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/95384317/258623925-69f2cd77-92ac-4162-97d0-ec013f141bf8.png" width="30">
  </a>&emsp;
 <a href="https://www.linkedin.com/in/victor-rios-f/" target="_blank">
   <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/95384317/258623927-682a6a1a-3176-4694-be40-1ae3c46ee11b.png" width="30">
  </a>
</div>
