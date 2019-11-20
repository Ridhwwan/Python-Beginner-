import datetime
import time
import tkinter.messagebox
from turtle import *
setup()
tl =Turtle()


root = Tk

frame = Frame(root)
tkinter.messagebox.showinfo("Ridhwan's Pomodoro Clock", "WELCOME. \n CLICK OK TO CONTINUE" )

def start():

  minutes=0
  seconds=0
  interval=0

  while interval!=4:
    tl.clear()
    tl.write(str(interval).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))
    time.sleep(0.01)
    seconds = seconds +1
    if seconds==60:
      seconds=0
      minutes+=1
    elif minutes == 20:
      seconds=0
      minutes=0
      interval+=1


    if interval ==4:
       tkinter.messagebox.showinfo("Ridhwan's Pomodoro Clock", "SCAT. SEE YOU IN 30 MINUTES")
       while minutes !=30:
         tl.clear()
         tl.write(str(minutes).zfill(2) + ':' + str(seconds).zfill(2))
         time.sleep(0.01)
         seconds = seconds +1
         if seconds==60:
           seconds=0
           minutes+=1
         elif minutes == 30:
           seconds=0
           minutes=0
           print("It is over")

answer = tkinter.messagebox.askquestion("Begin Task", "WOULD YOU LIKE TO START THE CLOCK?")

if answer == "yes":
  print(start)

'''
class Controls:
  def __init__(self,options):
    frame = Frame(options)
    frame.pack()

    self.Start = Button(frame, text= "START", command=self.printMessage)
    self.Start.grid(row='0',column='0', sticky='W', padx=4)

    self.Start = Button(frame, text= "RESTART", command=self.printMessage)
    self.Start.grid(row='0',column='1', sticky='W', padx=4)

    self.Start = Button(frame, text= "END", command=self.frame.quit)
    self.Start.grid(row='0',column='2', sticky='W', padx=4)


c = Controls(root)
'''





startt = Button(root, text="START", command=start).grid(row='0',column='0', sticky='W', padx=4)
startt.bind("<Button-1>", start)
restartt = Button(root, text="RESTART", command=start).grid(row='0',column='1', sticky='W', padx=4)
startt.bind("<Button-1>", start)
stopp = Button(root, text="END" , command=frame.quit).grid(row='0',column='2', sticky='W', padx=4)
startt.bind("<Button-1>", command=frame.quit)


root.mainloop()
    
