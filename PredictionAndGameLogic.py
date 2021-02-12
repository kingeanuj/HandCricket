from tensorflow.keras.models import model_from_json
import operator
import cv2
import random

#user bowling first
def bowl():
    json_file = open("model2.json", "r")
    model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(model_json)
    # load weights into new model
    loaded_model.load_weights("model2.h5")
    print("Good to go")
    
    cap = cv2.VideoCapture(0)
    
    categories = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',6:"SIX"}
    
    user_digit= None
    cpu_digit = None
    target = 0 
    user_score = 0
    cpu_score = 0
    flag = None
    flag1= None
    winner = []
    
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        x1 = int(0.5*frame.shape[1])
        y1 = 10
        x2 = frame.shape[1]-10
        y2 = int(0.5*frame.shape[1])

        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (0,0,255) ,2)
        

        roi = frame[y1:y2, x1:x2]
        
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
        cv2.putText(frame, "Press a if you are bowling", (20, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)
        cv2.putText(frame, "Press b if you are batting", (20, 460), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)
        
        cv2.putText(frame, "User: ", (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)    
        cv2.putText(frame, "CPU: ", (50, 170), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
        cv2.putText(frame, "Target: ", (20, 240), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
        cv2.putText(frame, str(user_score), (150, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)    
        cv2.putText(frame, str(cpu_score), (150, 170), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
        cv2.putText(frame, str(target), (150, 240), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
        
        
    
        cv2.imshow("Frame", frame)
        
            
        while cv2.waitKey(10) & 0xFF == ord('a') and flag != "out":
            prediction = {'0': result[0][0], 
                     '1': result[0][1], 
                     '2': result[0][2],
                     '3': result[0][3],
                     '4': result[0][4],
                     '6': result[0][5]}
            
            prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)

            user_digit = prediction[0][0]
            digits = [0,1,2,3,4,6]
            cpu_digit = random.choice(digits)
            print("User: {} CPU: {}".format(user_digit, cpu_digit))
            
            cpupic = cv2.imread("ImagesCPU/{}.jpg".format(str(cpu_digit)),-1) 
            cv2.putText(cpupic, str(cpu_digit), (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
            cv2.imshow(winname = "CPU", mat = cpupic)
            
            hand_digit = int(user_digit)
            if hand_digit != cpu_digit:
                cpu_score += cpu_digit
                continue
    
            if hand_digit == cpu_digit:
                print("\nCPU is out")
                flag = "out"
                print("Your target is {} runs".format(cpu_score+1))
                target = cpu_score+1
                break
            
            
        if user_score > cpu_score:
            winner.append("User")
            cv2.putText(frame, "Congrats you won!", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3)
            print("You won!")
            break
        
        if user_score < cpu_score and flag1 == "out":
            winner.append("CPU")
            cv2.putText(frame, "Oops you lost!", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3)
            print("CPU won")
            break
            
        if user_score == cpu_score and flag1 == "out":
            winner.append ("None")
            cv2.putText(frame, "Oops its a tie!", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3)
            print("Its a tie")
            break
            
            
        
        while cv2.waitKey(10) & 0xFF == ord('b') and flag == "out" and user_score <= cpu_score:
            
            prediction = {'0': result[0][0], 
                     '1': result[0][1], 
                     '2': result[0][2],
                     '3': result[0][3],
                     '4': result[0][4],
                     '6': result[0][5]}
            
            prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True) 
            user_digit = prediction[0][0]
            digits = [0,1,2,3,4,6]
            cpu_digit = random.choice(digits)
            print("User: {} CPU: {}".format(user_digit, cpu_digit))
            
            cpupic = cv2.imread("ImagesCPU/{}.jpg".format(str(cpu_digit)),-1) 
            cv2.putText(cpupic, str(cpu_digit), (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
            cv2.imshow(winname = "CPU", mat = cpupic)
    
            hand_digit = int(user_digit)
            if hand_digit != cpu_digit:
                user_score += hand_digit
                continue
    
            if hand_digit == cpu_digit :
                print("\nYou are out")
                print("You have scored {} runs".format(user_score))
                flag1 = "out"
                break
            
        if cv2.waitKey(10) & 0xFF == 27: #ESC key
            break
            
    cap.release()
    cv2.destroyAllWindows()
    return winner,user_score,cpu_score
    
#User batting first
def bat():
    json_file = open("model2.json", "r")
    model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(model_json)
    loaded_model.load_weights("model2.h5")
    print("Good to go")
    
    cap = cv2.VideoCapture(0)
    categories = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',6:"SIX"}
    
    user_digit= None
    cpu_digit = None
    target = 0 
    user_score = 0
    cpu_score = 0
    flag = None
    flag1= None
    winner = []
    
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        
        x1 = int(0.5*frame.shape[1])
        y1 = 10
        x2 = frame.shape[1]-10
        y2 = int(0.5*frame.shape[1])
        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (0,0,255) ,2)
        roi = frame[y1:y2, x1:x2]
        roi = cv2.resize(roi, (64, 64)) 
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imshow("test", test_image)
        
        result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
        prediction = {'0': result[0][0], 
                      '1': result[0][1], 
                      '2': result[0][2],
                      '3': result[0][3],
                      '4': result[0][4],
                      '6': result[0][5]}
        cv2.putText(frame, "Press a if you are bowling", (20, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)
        cv2.putText(frame, "Press b if you are batting", (20, 460), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)  
        
        cv2.putText(frame, "User: ", (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)    
        cv2.putText(frame, "CPU: ", (50, 170), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
        cv2.putText(frame, "Target: ", (20, 240), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
        cv2.putText(frame, str(user_score), (150, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)    
        cv2.putText(frame, str(cpu_score), (150, 170), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
        cv2.putText(frame, str(target), (150, 240), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
    
        cv2.imshow("Frame", frame)
        
        while cv2.waitKey(10) & 0xFF == ord('b') and flag != "out":
            prediction = {'0': result[0][0], 
                     '1': result[0][1], 
                     '2': result[0][2],
                     '3': result[0][3],
                     '4': result[0][4],
                     '6': result[0][5]}
            
            prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
            user_digit = prediction[0][0]
            digits = [0,1,2,3,4,6]
            cpu_digit = random.choice(digits)
            print("User: {} CPU: {}".format(user_digit, cpu_digit))
            
            cpupic = cv2.imread("ImagesCPU/{}.jpg".format(str(cpu_digit)),-1) 
            cv2.putText(cpupic, str(cpu_digit), (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
            cv2.imshow(winname = "CPU", mat = cpupic)
            
            hand_digit = int(user_digit)
            if hand_digit != cpu_digit:
                user_score += hand_digit
                continue

            if hand_digit == cpu_digit:
                print("\nYou are out")
                flag = "out"
                print("You have to defend {} runs".format(user_score+1))
                target = user_score+1
                break
            
        if cpu_score > user_score:
            winner.append("CPU")
            print("CPU won!")
            cv2.putText(frame, "Oops you lost!", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3)
            break
        
        if user_score > cpu_score and flag1 == "out":
            winner.append("User")
            cv2.putText(frame, "Congrats you won!", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3)
            print("You won")
            break
            
        if user_score == cpu_score and flag1 == "out":
            winner.append("None")
            cv2.putText(frame, "Oops its a tie!", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3)
            print("Its a tie")
            break
    
            
        
        while cv2.waitKey(10) & 0xFF == ord('a') and flag == "out" and cpu_score <= user_score:
            
            prediction = {'0': result[0][0], 
                     '1': result[0][1], 
                     '2': result[0][2],
                     '3': result[0][3],
                     '4': result[0][4],
                     '6': result[0][5]}

            prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True) 
            user_digit = prediction[0][0]
            digits = [0,1,2,3,4,6]
            cpu_digit = random.choice(digits)
            print("User: {} CPU: {}".format(user_digit, cpu_digit))  
            cpupic = cv2.imread("ImagesCPU/{}.jpg".format(str(cpu_digit)),-1) 
            cv2.putText(cpupic, str(cpu_digit), (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
            cv2.imshow(winname = "CPU", mat = cpupic)
    
            hand_digit = int(user_digit)
            if hand_digit != cpu_digit:
                cpu_score += cpu_digit
                continue
    
            if hand_digit == cpu_digit :
                print("\nCPU is out")
                flag1 = "out"
                break
            
        if cv2.waitKey(10) & 0xFF == 27: # ESC key
            break
            
 
    cap.release()
    cv2.destroyAllWindows()
    return winner, user_score,cpu_score
    
    
