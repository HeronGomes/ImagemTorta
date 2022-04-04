# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

imagem = cv.imread("Quadro5.jpg")
imagem = cv.resize(imagem,(400,600))

linha,coluna,canais = imagem.shape


back = np.full((linha,coluna,3),(0,0,0),np.uint8)  

for l in range(linha):
    for c in range(coluna):
        
        x = int(35 * np.sin(1.5*np.pi*l/180))
        
        if( x+c < coluna):
            back[l,c] = imagem[l,(x+c)]
        else:
            back[l,c] = imagem[l,c]
            


rodape = np.full((50,400,3),(0,0,0),dtype = np.uint8)
cv.putText(rodape,'As Ondas: Heron TF Gomes',(80,25),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.8,(190,190,190),1,cv.LINE_AA )
cv.putText(rodape,'06/08/2020',(290,45),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.5,(190,190,190),1,cv.LINE_AA )


resultado = cv.vconcat([back,rodape])

cv.imshow("Quadro",resultado)

cv.waitKey()
cv.destroyAllWindows()





cv.imwrite("Quadro5Ondas.png",resultado)