import keyboard
import atexit
from tkinter import *

root = Tk()
root.title("hot-key-board")
root.geometry("550x220")

keyDict = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
    '-':0,
    '=':0,
    '×':0,
    '÷':0,
    'esc':0,
    '`':0,
    'tab':0,
    'caps lock':0,
    'shift':0,
    'ctrl':0,
    'alt':0,
    'space':0,
    'enter':0,
    'backspace':0,
    '\\':0,
    ']':0,
    '[':0,
    '\'':0,
    ';':0,
    '/':0,
    '.':0,
    ',':0,
    'up':0,
    'down':0,
    'left':0,
    'right':0,
    'insert':0,
    'delete':0,
    'unknown':0,
}

def getBgCol(val):
    if val == 0:
        return '#000000'
    if val < 0.1:
        return '#26f34d'
    if val < 0.3:
        return '#36f326'
    if val < 0.4:
        return '#9af326'
    if val < 0.5:
        return '#ebf326'
    if val < 0.7:
        return '#f3bb26'
    if val < 0.9:
        return '#f37326'
    return '#f32626'

def showHotKeyBoard():
    try:
        factor=1.0/sum(keyDict.values())
        for key in keyDict:
            keyDict[key] = keyDict[key]*factor
        
        # print(keyDict)
            
        btnQ = Button(root, text = 'Q', bd = '5', bg = getBgCol(keyDict['q']))
        btnW = Button(root, text = 'W', bd = '5', bg = getBgCol(keyDict['w']))
        btnE = Button(root, text = 'E', bd = '5', bg = getBgCol(keyDict['e']))
        btnR = Button(root, text = 'R', bd = '5', bg = getBgCol(keyDict['r']))
        btnT = Button(root, text = 'T', bd = '5', bg = getBgCol(keyDict['t']))
        btnY = Button(root, text = 'Y', bd = '5', bg = getBgCol(keyDict['y']))
        btnU = Button(root, text = 'U', bd = '5', bg = getBgCol(keyDict['u']))
        btnI = Button(root, text = 'I', bd = '5', bg = getBgCol(keyDict['i']))
        btnO = Button(root, text = 'O', bd = '5', bg = getBgCol(keyDict['o']))
        btnP = Button(root, text = 'P', bd = '5', bg = getBgCol(keyDict['p']))
        btnA = Button(root, text = 'A', bd = '5', bg = getBgCol(keyDict['a']))
        btnS = Button(root, text = 'S', bd = '5', bg = getBgCol(keyDict['s']))
        btnD = Button(root, text = 'D', bd = '5', bg = getBgCol(keyDict['d']))
        btnF = Button(root, text = 'F', bd = '5', bg = getBgCol(keyDict['f']))
        btnG = Button(root, text = 'G', bd = '5', bg = getBgCol(keyDict['g']))
        btnH = Button(root, text = 'H', bd = '5', bg = getBgCol(keyDict['h']))
        btnJ = Button(root, text = 'J', bd = '5', bg = getBgCol(keyDict['j']))
        btnK = Button(root, text = 'K', bd = '5', bg = getBgCol(keyDict['k']))
        btnL = Button(root, text = 'L', bd = '5', bg = getBgCol(keyDict['l']))
        btnZ = Button(root, text = 'Z', bd = '5', bg = getBgCol(keyDict['z']))
        btnX = Button(root, text = 'X', bd = '5', bg = getBgCol(keyDict['x']))
        btnC = Button(root, text = 'C', bd = '5', bg = getBgCol(keyDict['c']))
        btnV = Button(root, text = 'V', bd = '5', bg = getBgCol(keyDict['v']))
        btnB = Button(root, text = 'B', bd = '5', bg = getBgCol(keyDict['b']))
        btnN = Button(root, text = 'N', bd = '5', bg = getBgCol(keyDict['n']))
        btnM = Button(root, text = 'M', bd = '5', bg = getBgCol(keyDict['m']))

        btnQ.place(x=10, y=10)
        btnW.place(x=60, y=10)
        btnE.place(x=110, y=10)
        btnR.place(x=160, y=10)
        btnT.place(x=210, y=10)
        btnY.place(x=260, y=10)
        btnU.place(x=310, y=10)
        btnI.place(x=360, y=10)
        btnO.place(x=410, y=10)
        btnP.place(x=460, y=10)
        btnA.place(x=35, y=60)
        btnS.place(x=95, y=60)
        btnD.place(x=145, y=60)
        btnF.place(x=195, y=60)
        btnG.place(x=245, y=60)
        btnH.place(x=295, y=60)
        btnJ.place(x=345, y=60)
        btnK.place(x=395, y=60)
        btnL.place(x=445, y=60)
        btnZ.place(x=60, y=110)
        btnX.place(x=110, y=110)
        btnC.place(x=160, y=110)
        btnV.place(x=210, y=110)
        btnB.place(x=260, y=110)
        btnN.place(x=310, y=110)
        btnM.place(x=360, y=110)

        mainloop()
    except:
        pass
    
atexit.register(showHotKeyBoard)

while True:
    try:
        key = keyboard.read_key()
        if key != 'unknown':
            keyDict[keyboard.read_key()] += 1
    except:
        showHotKeyBoard()
        break