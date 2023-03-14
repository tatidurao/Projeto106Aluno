import cv2
import numpy as np

# Crie nosso classificador de corpos
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Passe o quadro para nosso classificador de corpos
    #bodies = body.detectMultiScale(gray, 1.2, 3)
    #bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    #bodies = body_classifier.detectMultiScale(gray)
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    for (x,y,w,h) in bodies:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        #cv2.(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        #cv2.rectangle((x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestres', frame)

    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()