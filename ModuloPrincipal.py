import pandas as pd
from PIL import ImageDraw,Image,ImageFont
import face_recognition
import pygame
import datetime
from Funcionalidades import tomarFotos, Identificar

datos = pd.read_csv('./Archivos/datos.csv',sep=';')

print(datos.to_string())

#Convierto cada columna de datos del csv en una lista
nombres = datos['Nombre'].tolist()
apellidos = datos['Apellido'].tolist()
fotos = datos['Ruta Foto'].tolist()

canti = len(nombres)

usuarios = []
usuariosCodificado = []

for i in range(canti):

    usuarios.append(face_recognition.load_image_file(fotos[i]))
    usuariosCodificado.append(face_recognition.face_encodings(usuarios[i])[0])

Camara = tomarFotos()

ukFace = face_recognition.load_image_file('./CarpetaBasura/Usuario5.png')

resultadoComparacion = Identificar(usuariosCodificado,ukFace,canti)
print("la persona es: ",nombres[resultadoComparacion])


