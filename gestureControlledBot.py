import cv2
import numpy as np
import serial

ssc32 = serial.Serial('COM6', 9600, timeout=0)
#time.sleep(2)

fist = cv2.CascadeClassifier('fist.xml')
cap=cv2.VideoCapture(0)
while(1):
    

    fcx=0
    fcy=0
    #data="b"
    
    ret, img=cap.read()
    Y,X,channels=img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.line(img,(X//3,0),(X//3,Y),(255,255,225),2)
    cv2.line(img,(0,Y//3),(X,Y//3),(255,255,255),2)
    cv2.line(img,(2*X//3,0),(2*X//3,Y),(0,255,225),2)
    cv2.line(img,(0,2*Y//3),(X,2*Y//3),(0,255,255),2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'Forward',(X//3,Y//6-40), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(img,'Right',(2*X//3,260), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(img,'Left',(0,260), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(img,'bottom',(X//3,2*Y//3+100), font, 1,(0,255,0),2,cv2.LINE_AA)
    
    
    fistnew =fist.detectMultiScale(gray ,1.3,5)
    for (x,y,w,h) in fistnew:
        cv2.rectangle(img ,(x,y),(x+w,y+h),(255,0,0),2)
        fcx= x+w//2
        fcy= y+h//2
        cv2.circle(img,(fcx,fcy), 3, (0,0,255), -1)

    if(fcx!=0) :                  

                if (fcx <2*X//3 and fcx >X//3 and fcy<Y//3):
                    cv2.putText(img,'Forward',(X//3,Y//6-40), font, 1,(0,0,255),2,cv2.LINE_AA)
                    data= str(2)
                elif (fcx <2*X//3 and fcx >X//3 and fcy>2*Y//3):
                    cv2.putText(img,'Bottom',(X//3,2*Y//3+100), font, 1,(0,0,255),2,cv2.LINE_AA)
                    data= str(4)
                elif (fcy<2*Y//3 and fcy >Y//3 and fcx>2*X//3):
                    cv2.putText(img,'Right',(2*X//3,260), font, 1,(0,0,255),2,cv2.LINE_AA)
                    data= str(1)
                elif (fcy<2*Y//3 and fcy >Y//3 and fcx<X//3):
                    cv2.putText(img,'Left',(0,260), font, 1,(0,0,255),2,cv2.LINE_AA)
                    data= str(3)
                else:
                    data=str(0)
               
                
                bytes = str.encode(data)
                ssc32.write(bytes)
                print (ssc32.readline())
                ssc32.flush()
              

       
    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break    
        

cap.release()
cv2.destroyAllWindows()




