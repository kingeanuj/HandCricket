from tensorflow.keras.models import model_from_json
import operator
import cv2
import random


# Loading the model
json_file = open("model.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)

# Category dictionary
categories = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',6:"SIX"}



user_digit= None
cpu_digit = None
target = None



while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Got this from collect-data.py
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (0,0,255) ,2)
    
    
    
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    
    # Resizing the ROI so it can be fed to the model for prediction
    roi = cv2.resize(roi, (64, 64)) 
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)
    
   
    
    # Batch of 1
    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
    prediction = {'0': result[0][0], 
                  '1': result[0][1], 
                  '2': result[0][2],
                  '3': result[0][3],
                  '4': result[0][4],
                  '6': result[0][5]}
    cv2.putText(frame, "HAND CRICKET ", (20, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0), 3)    
    
    cv2.putText(frame, "User: ", (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)    
    cv2.putText(frame, "CPU: ", (50, 170), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
    cv2.putText(frame, "Target: ", (50, 240), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
    
    cv2.putText(frame, str(user_digit), (150, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)    
    cv2.putText(frame, str(cpu_digit), (150, 170), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3) 
    cv2.putText(frame, str(target), (150, 240), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
    
    cv2.putText(frame, str(user_digit), (460, 350), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3)
    cv2.imshow("Frame", frame)
    

    while cv2.waitKey(10) & 0xFF == ord('a'):
        # Sorting based on top prediction
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        
        # Displaying the predictions
        user_digit = prediction[0][0]
        digits = [0,1,2,3,4,6]
        cpu_digit = random.choice(digits)
        print("User: {} CPU: {}".format(user_digit, cpu_digit))
        
        cpupic = cv2.imread("ImagesCPU/{}.jpg".format(str(cpu_digit)),-1) 
        cv2.putText(cpupic, str(cpu_digit), (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
        cv2.imshow(winname = "CPU", mat = cpupic)
    

    if cv2.waitKey(10) & 0xFF == 27: # esc key
        break
        
 
cap.release()
cv2.destroyAllWindows()