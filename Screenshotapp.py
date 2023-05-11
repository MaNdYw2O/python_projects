import pyautogui
import tkinter as tk
import time
from unicodedata import name #for taking new data name
#pip insatll pyautogui
#pip install Pillow
#here are some important libraries u need to install
def screenshot():
    name = time.time() # name will change time to time
    #time.sleep(5)
    name = "D:/{}.png".format(name) #name of folder you want to save using .format functions
    img = pyautogui.screenshot() #calling object creation 
    img.save(name)    #saving name of the image
    img.show()  #here we call show function to show the image

root = tk.Tk()
frame = tk.Frame(root) # creating frame
frame.pack()
 
button = tk.Button(frame, text="Take Screenshot", command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="Quit", command=quit)
close.pack(side=tk.LEFT)

root.mainloop()



#screenshot()     #here we call our function