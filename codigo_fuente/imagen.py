import requests

url_imagen = "https://www.agenciapi.co/sites/default/files/styles/foto_noticia_principal/public/2018-12/Navidad.jpg?h=c673cd1c&itok=-QlN6Qwl" # El link de la imagen
nombre_local_imagen = "navidad.jpg" # El nombre con el que queremos guardarla
imagen = requests.get(url_imagen).content
with open(nombre_local_imagen, 'wb') as handler:
	handler.write(imagen)