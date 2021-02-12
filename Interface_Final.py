import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import PredictionAndGameLogic
import random

win = tk.Tk()
win.title('HAND CRICKET GAME')
win.geometry("1920x1280")
win['bg']='black'

#GameLabel
Labelwfont = ('times', 50, 'italic')
Labelw = tk.Label(win, text = "HAND CRICKET GAME✌", fg = "#FFFFFF", bg='#000000')
Labelw.config(font = Labelwfont)
Labelw.place(x=400,y=30)

def cpu_batting_first():
    winner,user_score,cpu_score = PredictionAndGameLogic.bowl()
    win4 = tk.Tk()
    win4.title('HAND CRICKET GAME')
    win4.geometry("1920x1280")
    win4['bg']='black'
    #GameLabel
    Labelwfont = ('times', 50, 'italic')
    Labelw = tk.Label(win4, text = "HAND CRICKET GAME✌", fg = "#FFFFFF", bg='#000000')
    Labelw.config(font = Labelwfont)
    Labelw.place(x=400,y=30)
    
    lblfont = ('times', 30)
    lbl = tk.Label(win4, text = "User: {}".format(user_score))
    lbl.config(font = lblfont)
    lbl.place(x=500, y= 400)
    
    lblfont = ('times', 30)
    lbl = tk.Label(win4, text = "CPU: {}".format(cpu_score))
    lbl.config(font = lblfont)
    lbl.place(x=800, y= 400)
    
    lblfont = ('times', 30)
    lbl = tk.Label(win4, text = "Winner : {}".format(winner[0]))
    lbl.config(font = lblfont)
    lbl.place(x=630, y= 300)
    
def cpu_bowling_first():
    
    winner,user_score,cpu_score = PredictionAndGameLogic.bat()
    win4 = tk.Tk()
    win4.title('HAND CRICKET GAME')
    win4.geometry("1920x1280")
    win4['bg']='black'
    #GameLabel
    Labelwfont = ('times', 50, 'italic')
    Labelw = tk.Label(win4, text = "HAND CRICKET GAME✌", fg = "#FFFFFF", bg='#000000')
    Labelw.config(font = Labelwfont)
    Labelw.place(x=400,y=30)
    
    lblfont = ('times', 30)
    lbl = tk.Label(win4, text = "User: {}".format(user_score))
    lbl.config(font = lblfont)
    lbl.place(x=500, y= 400)
    
    lblfont = ('times', 30)
    lbl = tk.Label(win4, text = "CPU: {}".format(cpu_score))
    lbl.config(font = lblfont)
    lbl.place(x=800, y= 400)
    
    lblfont = ('times', 30)
    lbl = tk.Label(win4, text = "Winner : {}".format(winner[0]))
    lbl.config(font = lblfont)
    lbl.place(x=630, y= 300)
    
def toss_head():
    win_third = tk.Tk()
    win_third.geometry("1920x1280")
    win_third['bg']='black'
    Labelwfont = ('times', 50, 'italic')
    Labelw = tk.Label(win_third, text = "HAND CRICKET GAME✌", fg = "#FFFFFF", bg='#000000')
    Labelw.config(font = Labelwfont)
    Labelw.place(x=400,y=30)
    
    user_toss_input = "head"
    bat_or_bowl = ["bat", "bowl"]
    toss = ["head", "tail"]
    toss_result = random.choice(toss)
    if user_toss_input == toss_result :
        
        lblfont = ('times', 30)
        lbl = tk.Label(win_third, text = "Congratulations! You have won the toss!")
        lbl.config(font = lblfont)
        lbl.place(x=440, y= 230)
        #asking label
        Label1font = ('times', 30)
        Label1 = tk.Label(win_third, text = "Choose Batting or Bowling!")
        Label1.config(font = Label1font)
        Label1.place(x=525, y=360)
        
        myFont = font.Font(family='times',size=20)
        button1 = tk.Button(win_third,text = "BAT", command = cpu_bowling_first, height = 2, width = 15,fg = "#FFFFFF", bg= 	'#000000')
        button1['font'] = myFont
        button1.place(x=530, y= 460)
        
        myFont = font.Font(family='times',size=20)
        button2 = tk.Button(win_third,text = "BOWL", command = cpu_batting_first, height = 2, width = 15,fg = "#FFFFFF", bg= 	'#000000')
        button2['font'] = myFont
        button2.place(x=800, y= 460)
        
    else:
        print("You have lost the toss")
        cpu_action = random.choice(bat_or_bowl)
        lblfont = ('times', 30)
        lbl = tk.Label(win_third, text = "Oops! You have lost the toss!")
        lbl.config(font = lblfont)
        lbl.place(x=530, y= 230)
        lbl = tk.Label(win_third, text = "CPU will {} first!".format(cpu_action))
        lbl.config(font = lblfont)
        lbl.place(x=600, y= 310)
        print("\nCPU will {} first".format(cpu_action))
        
        if cpu_action == "bat":
            play_button = tk.Button(win_third, text='PLAY',command= cpu_batting_first, height = 2, width = 15,fg = "#FFFFFF", bg='#000000' )
            myFont2 = font.Font(family='times',size=25)
            play_button['font'] = myFont2
            play_button.place(x=660, y= 450)
        else:
            play_button = tk.Button(win_third, text='PLAY',command= cpu_bowling_first, height = 2, width = 15,fg = "#FFFFFF", bg='#000000' )
            myFont2 = font.Font(family='times',size=25)
            play_button['font'] = myFont2
            play_button.place(x=660, y= 450)

def toss_tail():
    win_third = tk.Tk()
    win_third.geometry("1920x1280")
    win_third['bg']='black'
    Labelwfont = ('times', 50, 'italic')
    Labelw = tk.Label(win_third, text = "HAND CRICKET GAME✌", fg = "#FFFFFF", bg='#000000')
    Labelw.config(font = Labelwfont)
    Labelw.place(x=400,y=30)
    
    user_toss_input = "tail"
    bat_or_bowl = ["bat", "bowl"]
    toss = ["head", "tail"]
    toss_result = random.choice(toss)
    if user_toss_input == toss_result :
        
        lblfont = ('times', 30)
        lbl = tk.Label(win_third, text = "Congratulations! You have won the toss!")
        lbl.config(font = lblfont)
        lbl.place(x=440, y= 230)
        #asking label
        Label1font = ('times', 30)
        Label1 = tk.Label(win_third, text = "Choose Batting or Bowling!")
        Label1.config(font = Label1font)
        Label1.place(x=525, y=360)
        
        myFont = font.Font(family='times',size=20)
        button1 = tk.Button(win_third,text = "BAT", command = cpu_bowling_first, height = 2, width = 15,fg = "#FFFFFF", bg= 	'#000000')
        button1['font'] = myFont
        button1.place(x=530, y= 460)
        
        myFont = font.Font(family='times',size=20)
        button2 = tk.Button(win_third,text = "BOWL", command = cpu_batting_first, height = 2, width = 15,fg = "#FFFFFF", bg= 	'#000000')
        button2['font'] = myFont
        button2.place(x=800, y= 460)
        
      
    else:
        print("You have lost the toss")
        cpu_action = random.choice(bat_or_bowl)
        lblfont = ('times', 30)
        lbl = tk.Label(win_third, text = "Oops! You have lost the toss!")
        lbl.config(font = lblfont)
        lbl.place(x=530, y= 230)
        lbl = tk.Label(win_third, text = "CPU will {} first!".format(cpu_action))
        lbl.config(font = lblfont)
        lbl.place(x=600, y= 310)
        print("\nCPU will {} first".format(cpu_action))
        
        if cpu_action == "bat":
            play_button = tk.Button(win_third, text='PLAY',command= cpu_batting_first, height = 2, width = 15,fg = "#FFFFFF", bg='#000000' )
            myFont2 = font.Font(family='times',size=25)
            play_button['font'] = myFont2
            play_button.place(x=660, y= 450)
        else:
            play_button = tk.Button(win_third, text='PLAY',command= cpu_bowling_first, height = 2, width = 15,fg = "#FFFFFF", bg='#000000' )
            myFont2 = font.Font(family='times',size=25)
            play_button['font'] = myFont2
            play_button.place(x=660, y= 450)

def Play():
    win_second = tk.Tk()
    win_second.geometry("1920x1280")
    win_second['bg']='black'
    Labelwfont = ('times', 50, 'italic')
    Labelw = tk.Label(win_second, text = "HAND CRICKET GAME✌", fg = "#FFFFFF", bg='#000000')
    Labelw.config(font = Labelwfont)
    Labelw.place(x=400,y=30)
    
    #back button
    back_button = tk.Button(win_second, text='BACK', command=win_second.destroy, height = 2, width = 15,fg = "#FFFFFF", bg='#000000' )
    myFont2 = font.Font(family='times',size=25)
    back_button['font'] = myFont2
    back_button.place(x=660, y= 560)
    
    #asking label
    Label1font = ('times', 30)
    Label1 = tk.Label(win_second, text = "Choose Head or Tail!")
    Label1.config(font = Label1font)
    Label1.place(x=590, y=230)
    
    myFont = font.Font(family='times',size=20)
    button1 = tk.Button(win_second,text = "HEAD", command = toss_head, height = 2, width = 15,fg = "#FFFFFF", bg= 	'#000000')
    button1['font'] = myFont
    button1.place(x=530, y= 330)
    
    myFont = font.Font(family='times',size=20)
    button2 = tk.Button(win_second,text = "TAIL", command = toss_tail, height = 2, width = 15,fg = "#FFFFFF", bg= 	'#000000')
    button2['font'] = myFont
    button2.place(x=800, y= 330)

#Play button
myFont = font.Font(family='times',size=20)
button = tk.Button(text = "PLAY", command = Play, height = 2, width = 15,fg = "#FFFFFF", bg= 	'#000000')
button['font'] = myFont
button.place(x=630, y= 230)

# Rules function
def Rules():
    win_rules = tk.Tk()
    win_rules.geometry("1920x1280")
    win_rules['bg']='black'
    
    Label1font = ('times', 15)
    Label1 = tk.Label(win_rules, text = """
HAND CRICKET ✌

Hand Cricket is an immensly popular game which is played between 
two people. It is a derivative of the most common rock, paper & scissors. 
The school going children love this game thanks to it being so
easy to play. Now in this game two players show scores using their 
respective fingers. If the two scores are equal, the batsman is declared
out. Else the score is added to the batsman's total score.

RULES :
1) We need just 2 players. In this case, The user and the AI.
2) Now for the toss. The user selects heads or tails. The CPU randomly 
picks heads or tales and shows wether the user has won or lost the toss. 
3)The winner of the toss chooses to either "Bat" or "Bowl"
4)The most inportant part. Name says it all. So here is how you should represent each number
For 0, just don't show anything. 
For 1, just throw your hand with ONLY your index finger extended, and the others clenched into a fist.
For 2, just throw 'scissors'.
For 3, just extend your middle, ring and index fingers.
For 4, just add your little finger to the three.
For 6, throw a clenched fist with your thumb extended.
5)Batting and Wickets
Both of them show their hands at the same time. If the numbers are same, the batsman is out. If
the numbers are different. The batsman's number get's added to his total score. 
6)Winning:
	The person with the highest score at the end wins.""", fg = "#FFFFFF", bg='#000000')
    Label1.config(font = Label1font)
    Label1.place(x=310, y=50)
    
    
    back_button = tk.Button(win_rules, text='BACK', command=win_rules.destroy, height = 2, width = 15,fg = "#FFFFFF", bg='#000000' )
    myFont2 = font.Font(family='times',size=25)
    back_button['font'] = myFont2
    back_button.place(x=640, y= 660)

#Rules button
button2 = tk.Button(text = "RULES",command = Rules, height = 2, width = 15,fg = "#FFFFFF", bg= 	'#000000')
button2['font'] = myFont
button2.place(x=630, y= 340)

#About us function
def about():
    win_about = tk.Tk()
    win_about.geometry("1920x1280")
    win_about['bg']='black'
    
    Label1font = ('times', 15)
    Label1 = tk.Label(win_about, text = """ABOUT

The game "Hand Cricket" has been designed by us using gesture recognition. 
Gesture recognition is a technology which uses optical character
recognition to identify gestures, hand movements etc. It has seen
application on various platforms like VR, AR, Gaming consoles (Xbox
Kinect) etc. The game of hand cricket has been very popular among
school going children. The Corona outbreak has affected social
interaction. The project will allow the person to play a game of hand
cricket against the computer. The project will use gesture recognition in
real time similar to that found in gaming consoles. 
Libraries like OpenCV help in real-time computer vision, Convolutional
Neural Network or CNN help in analyzing the image. TensorFlow and
Keras for machine learning and the framework.

Creators of this application:
Anuj Kinge 
(BTech CSE MIT-ADT University) 
Aditya Devchakke 
(BTech CSE MIT-ADT University) 
Aditya Dawda 
(BTech CSE MIT-ADT University) 
Ankit Mukopadhyay 
(BTech CSE MIT-ADT University) """, fg = "#FFFFFF", bg='#000000')
    Label1.config(font = Label1font)
    Label1.place(x=450, y=80)
    
    back_button = tk.Button(win_about, text='BACK', command=win_about.destroy, height = 2, width = 15,fg = "#FFFFFF", bg='#000000' )
    myFont2 = font.Font(family='times',size=25)
    back_button['font'] = myFont2
    back_button.place(x=660, y= 660)

#About us button
button3 = tk.Button(text = "ABOUT",command = about, height = 2, width = 15,fg = "#FFFFFF", bg='#000000')
button3['font'] = myFont
button3.place(x=630, y= 450)

#Exit function
def Exit():
    MsgBox = messagebox.askquestion ('Exit','Are you sure you want to exit?',icon = 'warning')
    if MsgBox == 'yes':
       win.destroy()
    else:
        pass

#Exit button
button4 = tk.Button(text = "EXIT", command = Exit, height = 2, width = 15,fg = "#FFFFFF", bg='#000000' )
button4['font'] = myFont
button4.place(x=630, y= 560)

win.mainloop()


