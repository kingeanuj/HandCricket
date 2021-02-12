import cv2
import os

#mode train or test
mode = 'train'                        
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    count = {'zero': len(os.listdir(directory+"/0")),
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'six' : len(os.listdir(directory+"/6"))}
    
    cv2.putText(frame, "MODE : "+mode, (100, 80), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
    cv2.putText(frame, "0 : "+str(count['zero']), (100, 120), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
    cv2.putText(frame, "1 : "+str(count['one']), (100, 140), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
    cv2.putText(frame, "2 : "+str(count['two']), (100, 160), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
    cv2.putText(frame, "3 : "+str(count['three']), (100, 180), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
    cv2.putText(frame, "4 : "+str(count['four']), (100, 200), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
    cv2.putText(frame, "6 : "+str(count['six']),(100,220),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
    
    x1 = 380
    y1 = 80
    x2 = 630
    y2 = 320
    
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (0,0,255) ,1)
   
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64)) 
    cv2.imshow("Frame", frame)
    
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # ESC key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg',roi)
    
cap.release()
cv2.destroyAllWindows()
