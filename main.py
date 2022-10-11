import keyboard
import atexit
from tkinter import *

root = Tk()
root.title("hot-key-board")
root.geometry("750x220")

buttonGap = 50
escapeKeys = ['unknown', 'help','f13','f14']

# key dictionary
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

# returns colors based on normalized value 
def getBgCol(val):
    if val == 0:
        return '#555555'
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

# vizualize at end
def showHotKeyBoard():
    try:
        factor=1.0/sum(keyDict.values())
        for key in keyDict:
            keyDict[key] = keyDict[key]*factor
        
        # print(keyDict)
        
        # buttons initialize
        btn1 = Button(root, text = '1', bd = '5', bg = getBgCol(keyDict['1']))
        btn2 = Button(root, text = '2', bd = '5', bg = getBgCol(keyDict['2']))
        btn3 = Button(root, text = '3', bd = '5', bg = getBgCol(keyDict['3']))
        btn4 = Button(root, text = '4', bd = '5', bg = getBgCol(keyDict['4']))
        btn5 = Button(root, text = '5', bd = '5', bg = getBgCol(keyDict['5']))
        btn6 = Button(root, text = '6', bd = '5', bg = getBgCol(keyDict['6']))
        btn7 = Button(root, text = '7', bd = '5', bg = getBgCol(keyDict['7']))
        btn8 = Button(root, text = '8', bd = '5', bg = getBgCol(keyDict['8']))
        btn9 = Button(root, text = '9', bd = '5', bg = getBgCol(keyDict['9']))
        btn0 = Button(root, text = '0', bd = '5', bg = getBgCol(keyDict['0']))
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
        btnMinus = Button(root, text = '-', bd = '5', bg = getBgCol(keyDict['-']))
        btnEquals = Button(root, text = '=', bd = '5', bg = getBgCol(keyDict['=']))
        btnSqBracetOpen = Button(root, text = '[', bd = '5', bg = getBgCol(keyDict['[']))
        btnSqBracetClose = Button(root, text = ']', bd = '5', bg = getBgCol(keyDict[']']))
        btnBackSlash = Button(root, text = '\\', bd = '5', bg = getBgCol(keyDict['\\']))
        btnSemiColon = Button(root, text = ';', bd = '5', bg = getBgCol(keyDict[';']))
        btnQuote = Button(root, text = '\'', bd = '5', bg = getBgCol(keyDict['\'']))
        btnComma = Button(root, text = ',', bd = '5', bg = getBgCol(keyDict[',']))
        btnDot = Button(root, text = '.', bd = '5', bg = getBgCol(keyDict['.']))
        btnSlash = Button(root, text = '/', bd = '5', bg = getBgCol(keyDict['/']))

        # button positioning
        btn1.place(x=10, y=10)
        btn2.place(x=10 + buttonGap, y=10)
        btn3.place(x=10 + 2*buttonGap, y=10)
        btn4.place(x=10 + 3*buttonGap, y=10)
        btn5.place(x=10 + 4*buttonGap, y=10)
        btn6.place(x=10 + 5*buttonGap, y=10)
        btn7.place(x=10 + 6*buttonGap, y=10)
        btn8.place(x=10 + 7*buttonGap, y=10)
        btn9.place(x=10 + 8*buttonGap, y=10)
        btn0.place(x=10 + 9*buttonGap, y=10)
        btnMinus.place(x=10 + 10*buttonGap, y=10)
        btnEquals.place(x=10 + 11*buttonGap, y=10)

        btnQ.place(x=35, y=10 + buttonGap)
        btnW.place(x=35 + buttonGap, y=10 + buttonGap)
        btnE.place(x=35 + 2*buttonGap, y=10 + buttonGap)
        btnR.place(x=35 + 3*buttonGap, y=10 + buttonGap)
        btnT.place(x=35 + 4*buttonGap, y=10 + buttonGap)
        btnY.place(x=35 + 5*buttonGap, y=10 + buttonGap)
        btnU.place(x=35 + 6*buttonGap, y=10 + buttonGap)
        btnI.place(x=35 + 7*buttonGap, y=10 + buttonGap)
        btnO.place(x=35 + 8*buttonGap, y=10 + buttonGap)
        btnP.place(x=35 + 9*buttonGap, y=10 + buttonGap)
        btnSqBracetOpen.place(x=35 + 10*buttonGap, y=10 + buttonGap)
        btnSqBracetClose.place(x=35 + 11*buttonGap, y=10 + buttonGap)
        btnBackSlash.place(x=35 + 12*buttonGap, y=10 + buttonGap)

        btnA.place(x=60, y=10 + 2*buttonGap)
        btnS.place(x=60 + buttonGap, y=10 + 2*buttonGap)
        btnD.place(x=60 + 2*buttonGap, y=10 + 2*buttonGap)
        btnF.place(x=60 + 3*buttonGap, y=10 + 2*buttonGap)
        btnG.place(x=60 + 4*buttonGap, y=10 + 2*buttonGap)
        btnH.place(x=60 + 5*buttonGap, y=10 + 2*buttonGap)
        btnJ.place(x=60 + 6*buttonGap, y=10 + 2*buttonGap)
        btnK.place(x=60 + 7*buttonGap, y=10 + 2*buttonGap)
        btnL.place(x=60 + 8*buttonGap, y=10 + 2*buttonGap)
        btnSemiColon.place(x=60 + 9*buttonGap, y=10 + 2*buttonGap)
        btnQuote.place(x=60 + 10*buttonGap, y=10 + 2*buttonGap)

        btnZ.place(x=85, y=10 + 3*buttonGap)
        btnX.place(x=85 + buttonGap, y=10 + 3*buttonGap)
        btnC.place(x=85 + 2*buttonGap, y=10 + 3*buttonGap)
        btnV.place(x=85 + 3*buttonGap, y=10 + 3*buttonGap)
        btnB.place(x=85 + 4*buttonGap, y=10 + 3*buttonGap)
        btnN.place(x=85 + 5*buttonGap, y=10 + 3*buttonGap)
        btnM.place(x=85 + 6*buttonGap, y=10 + 3*buttonGap)
        btnComma.place(x=85 + 7*buttonGap, y=10 + 3*buttonGap)
        btnDot.place(x=85 + 8*buttonGap, y=10 + 3*buttonGap)
        btnSlash.place(x=85 + 9*buttonGap, y=10 + 3*buttonGap)

        mainloop()
    except:
        pass

# run at exit 
atexit.register(showHotKeyBoard)

while True:
    try:
        key = keyboard.read_key()
        if key not in escapeKeys:
            keyDict[keyboard.read_key()] += 1
    except Exception as e:
        # print(e)
        showHotKeyBoard()
        break