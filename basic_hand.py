import cv2 as cv
import mediapipe as mp
import time 

cap= cv.VideoCapture(0)
mphands=mp.solutions.mediapipe.python.solutions.hands

hannd=mphands.Hands()

draw=mp.solutions.mediapipe.python.solutions.drawing_utils
pTime=0
cTime=0


while True:
    success,img= cap.read()
    img_rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result= hannd.process(img_rgb)

    # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handss in result.multi_hand_landmarks:
            # print(hands)
            for id,lm in enumerate(handss.landmark):
                #print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)

                print(id,cx,cy)

                if id==0:
                    cv.circle(img,(cx,cy),10,(255,0,255),cv.FILLED)
            draw.draw_landmarks(img,handss,mphands.HAND_CONNECTIONS)
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv.putText(img,str(int(fps)),(15,70),cv.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
    cv.imshow("image",img)

    cv.waitKey(1)