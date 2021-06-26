# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
import math
def rgb2hex(rgbcolor):
  r, g, b = rgbcolor
  return (r << 16) + (g << 8) + b

def color_finder(joy,relaxation,fear,sadness):
    joy_list={"0":[64,0,0],"0.25":[191,0,0],"0.5":[255,64,64],"0.75":[255,0,0]}
    relaxation_list={"0":[100, 245, 255],"0.25":[96,191,0],"0.5":[159,255,64],"0.75":[223,255,191]}
    fear_list = {"0": [100, 245, 255], "0.25": [191,128,255], "0.5": [96,0,191], "0.75": [32,0,64]}
    sadness_list = {"0": [100, 245, 255], "0.25": [128, 191, 255], "0.5": [0,128,255], "0.75": [0,0, 0]}
    return [math.floor((joy_list[joy][0]+relaxation_list[relaxation][0]+fear_list[fear][0]+sadness_list[sadness][0])/3),
            math.floor((245+joy_list[joy][1]+relaxation_list[relaxation][1]+fear_list[fear][1]+sadness_list[sadness][1])/4),
            math.floor((255+joy_list[joy][2]+relaxation_list[relaxation][2]+fear_list[fear][2]+sadness_list[sadness][2])/4)]


window = tkinter.Tk()
window.title("a rectangle")
text1 = tkinter.Label(window,text="joy")
text2 = tkinter.Label(window,text="relaxation")
text3 = tkinter.Label(window,text="fear")
text4 = tkinter.Label(window,text="sadness")
text5 = tkinter.Label(window,text="only 0 0.25 0.5 0.75 four numbers are available")
E1 = tkinter.Entry(window, bd=5)
E2 = tkinter.Entry(window, bd=5)
E3 = tkinter.Entry(window, bd=5)
E4 = tkinter.Entry(window, bd=5)
text1.pack()
E1.pack()
text2.pack()
E2.pack()
text3.pack()
E3.pack()
text4.pack()
E4.pack()
text5.pack()
canvas = tkinter.Canvas(window, width=800, height=500, bg="white")
def helloCallBack():
    window.update()
    joy=E1.get()
    relax = E2.get()
    fear = E3.get()
    sad = E4.get()
    color=color_finder(joy,relax,fear,sad)
    color=rgb2hex(color)
    canvas.create_rectangle(100, 100, 200, 200, fill="#" + str(hex(color)[2:]))
    canvas.pack()

B = tkinter.Button(text="generate", command=helloCallBack)
B.pack()

window.mainloop()
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def rgb2hex(rgbcolor):
  r, g, b = rgbcolor
  return (r << 16) + (g << 8) + b
'''
def color_finder(joy,relaxation,fear,sadness):
    joy_list={"0":[64,0,0],"0.25":[191,0,0],"0.5":[255,64,64],"0.75":[255,0,0]}
    relaxation_list={"0":[255, 255, 255],"0.25":[96,191,0],"0.5":[159,255,64],"0.75":[223,255,191]}
    fear_list = {"0": [255, 255, 255], "0.25": [191,128,255], "0.5": [96,0,191], "0.75": [32,0,64]}
    sadness_list = {"0": [255, 255, 255], "0.25": [128, 191, 255], "0.5": [0,128,255], "0.75": [0,0, 0]}
    return [math.floor((joy_list[joy][0]+relaxation_list[relaxation][0]+fear_list[fear][0]+sadness_list[sadness][0])/4),
            math.floor((245+joy_list[joy][1]+relaxation_list[relaxation][1]+fear_list[fear][1]+sadness_list[sadness][1])/4),
            math.floor((255+joy_list[joy][2]+relaxation_list[relaxation][2]+fear_list[fear][2]+sadness_list[sadness][2])/4)]

'''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
