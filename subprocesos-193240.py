from imgurpython import ImgurClient
from threading import *
import os
import urllib.request
import timeit
from concurrent import futures
import multiprocessing
 
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)
 
# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
 
 
def descarga_url_img(link):
   #print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "imagenes/{}.{}"
   #Guardar nne local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))

# def album():
#     id_album = "bUaCfoz"
#     return cliente.get_album_images(id_album)

def mythread():
    print("Hilos")
    id_album = "bUaCfoz"
    imagenes = cliente.get_album_images(id_album)
    for imagen in imagenes:
       child=Thread(target=descarga_url_img(imagen.link))
       child.start()
       print("Executing thread name :",current_thread().getName())

def Executor():
    print("Executor")
    id_album = "bUaCfoz"
    imagenes = cliente.get_album_images(id_album)
    links = []
    for imagen in imagenes:
      links.append(imagen.link)
    ex = futures.ThreadPoolExecutor(max_workers=10)
    ex.map(descarga_url_img, links)

def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
 
   for imagen in imagenes:
       descarga_url_img(imagen.link)
 
 
if __name__ == "__main__":
   print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))
   print("Tiempo de descarga {}".format(timeit.Timer(mythread).timeit(number=1)))
   print("Tiempo de descarga {}".format(timeit.Timer(Executor).timeit(number=1)))