from os import environ #Importa el diccionario completo con todas las variables de entorno como PATH, HOME, USERNAME, etc.
from os import pathsep #se utiliza para separar las diferentes rutas en la variable de entorno

""" 
\s+: Coincide con uno o más espacios en blanco.
\d+: Coincide con uno o más dígitos.
\w+: Coincide con una o más letras, dígitos o guiones bajos.
\b: Coincide con un límite de palabra.
[A-Za-z]+: Coincide con una o más letras mayúsculas o minúsculas.
[0-9]+: Coincide con uno o más dígitos.
[aeiou]+: Coincide con una o más vocales.
[^0-9]+: Coincide con uno o más caracteres que no sean dígitos.
\s{2,}: Coincide con dos o más espacios consecutivos.
[^\w\s]+: Coincide con uno o más caracteres que no sean letras, dígitos o espacios.
[A-Z][a-z]+: Coincide con una letra mayúscula seguida de una o más letras minúsculas.
\b\w{4}\b: Coincide con palabras de exactamente 4 letras.
[0-9]{2}-[0-9]{2}-[0-9]{4}: Coincide con una fecha en formato dd-mm-aaaa.
[a-zA-Z0-9]+: Coincide con una o más letras mayúsculas, minúsculas o dígitos.
[^\w\s]+: Coincide con uno o más caracteres que no sean letras, dígitos o espacios en blanco. 
"""