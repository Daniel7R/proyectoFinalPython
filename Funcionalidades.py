import face_recognition
import sys
import cv2
from face_recognition.api import face_encodings

def tomarFotos():

    camara = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    for i in range(10):
        
        valor,imagen = camara.read()
        #Asigno el nombre a las imagenes que se guardaran de manera temporal
        cv2.imwrite('./CarpetaBasura/Usuario'+str(i+1)+'.png',imagen)

        print(valor, imagen.shape)
    
    del(camara)


def Identificar(usuariosCodificados, ukface,cantidad):

    try:

        ukFaceEncode = face_recognition.face_encodings(ukface)[0]

    except IndexError as error:

        print("\nNo es posible codificar la foto, por favor tome una foto con mejor iluminación :)")
        sys.exit(1)
    
    
    resultado = face_recognition.compare_faces(usuariosCodificados,ukFaceEncode,tolerance=0.5)
    print("\nImprimiendo la lista de resultados: \n",resultado)

    indiceEncontrado = -1

    for i in range(cantidad):
        
        if resultado[i]:
            
            indiceEncontrado = i
    
    return indiceEncontrado