import cv2


camera = cv2.VideoCapture(0)

for i in range(10):
    valor,imagen = camera.read()
    print(valor,imagen.shape)
    cv2.imwrite("foto"+ str(i+1) + ".png", imagen)

del camera