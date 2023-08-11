""" Instalar el enterno virtual """
#pip install virtualenv


""" Crear Entorno virtual """
#virtualenv -p python3 env  //forma antigua externa
#virtualenv -p python3 myenv //Forma nueva nativa Compatible con python3
#python -m venv myenv //Forma nueva nativa Compatible con python3.3

""" Activar el entorno virtual """
#.\env\Scripts\activate
#.\myenv\Scripts\activate
#virtualenv venv .\ #si nos da error usar este para que sea absoluta
#virtualenv C: //forzar la ruta

""" Instalar Flask """
#pip install Flask
""" Instalar mysql """
#pip install mysql-connector-python

""" Crear backup de los paquetes """
#pip freeze > requirements.txt
""" Instalar nuevamente toda la lista de paquetes que teniamos """
#pip install -r .\requirements.txt //recomendado
#pip install -r requirements.txt


""" Error ejecucion de escripts esta deshabilitada """
""" Ver si tengo acceso al virtual env """
#Get-ExecutionPolicy
""" Dar permisos desde el Windows PowerShell (Admin) """
#Set-ExecutionPolicy RemoteSigned

""" Web escraping"""
""" 
data/: Aquí es donde puedes almacenar los archivos de datos utilizados en tu proyecto.
results/: En esta carpeta, puedes guardar los resultados generados por tu aplicación. 
src/: En esta carpeta, puedes colocar el archivo de notebook (notebook.ipynb) que contiene tu código principal. También puedes tener otros scripts Python 
utils/: En esta carpeta, puedes colocar funciones de utilidad, clases personalizadas o módulos adicionales que puedas necesitar en tu proyecto. 
"""

"""
#Jupyter
pip install jupyter_contrib_nbextensions # Instalar Jupyter-Notebook-Code-Formatter
jupyter contrib nbextension install --user # Habilita la extensión ejecutando el siguiente comando:
jupyter nbextension enable code_prettify/autopep8 #A ctiva la extensión de autocompletado ejecutando el siguiente comando:
#Reinicia tu servidor Jupyter Notebook para que te muestre opciones.
pip install autopep8 # Si no tienes instalado autopep8
conda update jupyter notebook # Actualiza el Jupyter Notebook
"""

""" 
PAQUETES PARA web escraping
pip install requests// nos permite manipular archivos ftp
pip install beautifulsoup4// nos permite procesar todos los datos del html para poder extraerlos
pip install selenium// nos permite automatizar todo
pip install pandas // nos permite acomodarlo en un excel por asi decirlo en tablas organizarlo todo
pip install openpyxl //nos permite trabajar con archivos Excel en pandas al momento de exportar.

"""
#import requests >>> Es para importar la libreria que nos permite utilizar solicitudes http
#from bs4 import BeautifulSoup >>>(bs4)Es una Biblioteca que nos convierte el archivo a un html
#r.status_code >>>(r.status_code == 200) Esta okey el estado
#r.content >>> Imprimir todo el contenido (no textual como archivos de imagen, archivos PDF u otros tipos)
#r.text >>> Imprimir todo el contenido (como una cadena de texto como HTML, JSON, XML)
# soup =BeatifulSoup(rcontent,'html.parser) >>> 
#//h2[@class = "ui-search-item__title shops__item-title"] >>> Buscar el elemento de html

#sep='|' >>>separame todo por un |