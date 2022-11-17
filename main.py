import keyboard
import atexit
from tkinter import *
import sys

root = Tk()
root.title("hot-key-board")
root.geometry("850x300")

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

# returns bg colors based on normalized value 
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

# returns fg colors based on normalized value 
def getFgCol(val):
    if val > 0:
        return '#000'
    return '#fff'

# vizualize at end
def showHotKeyBoard():
    try:
        total = sum(keyDict.values())

        if total == 0:
            total = 1

        factor=1.0/total
        for key in keyDict:
            keyDict[key] = keyDict[key]*factor
        
        # buttons initialize
        btnGrave = Button(root, text = '`', bd = '5', fg = getFgCol(keyDict['`']), bg = getBgCol(keyDict['`']))
        btn1 = Button(root, text = '1', bd = '5', fg = getFgCol(keyDict['1']), bg = getBgCol(keyDict['1']))
        btn2 = Button(root, text = '2', bd = '5', fg = getFgCol(keyDict['2']), bg = getBgCol(keyDict['2']))
        btn3 = Button(root, text = '3', bd = '5', fg = getFgCol(keyDict['3']), bg = getBgCol(keyDict['3']))
        btn4 = Button(root, text = '4', bd = '5', fg = getFgCol(keyDict['4']), bg = getBgCol(keyDict['4']))
        btn5 = Button(root, text = '5', bd = '5', fg = getFgCol(keyDict['5']), bg = getBgCol(keyDict['5']))
        btn6 = Button(root, text = '6', bd = '5', fg = getFgCol(keyDict['6']), bg = getBgCol(keyDict['6']))
        btn7 = Button(root, text = '7', bd = '5', fg = getFgCol(keyDict['7']), bg = getBgCol(keyDict['7']))
        btn8 = Button(root, text = '8', bd = '5', fg = getFgCol(keyDict['8']), bg = getBgCol(keyDict['8']))
        btn9 = Button(root, text = '9', bd = '5', fg = getFgCol(keyDict['9']), bg = getBgCol(keyDict['9']))
        btn0 = Button(root, text = '0', bd = '5', fg = getFgCol(keyDict['0']), bg = getBgCol(keyDict['0']))
        btnQ = Button(root, text = 'Q', bd = '5', fg = getFgCol(keyDict['q']), bg = getBgCol(keyDict['q']))
        btnW = Button(root, text = 'W', bd = '5', fg = getFgCol(keyDict['w']), bg = getBgCol(keyDict['w']))
        btnE = Button(root, text = 'E', bd = '5', fg = getFgCol(keyDict['e']), bg = getBgCol(keyDict['e']))
        btnR = Button(root, text = 'R', bd = '5', fg = getFgCol(keyDict['r']), bg = getBgCol(keyDict['r']))
        btnT = Button(root, text = 'T', bd = '5', fg = getFgCol(keyDict['t']), bg = getBgCol(keyDict['t']))
        btnY = Button(root, text = 'Y', bd = '5', fg = getFgCol(keyDict['y']), bg = getBgCol(keyDict['y']))
        btnU = Button(root, text = 'U', bd = '5', fg = getFgCol(keyDict['u']), bg = getBgCol(keyDict['u']))
        btnI = Button(root, text = 'I', bd = '5', fg = getFgCol(keyDict['i']), bg = getBgCol(keyDict['i']))
        btnO = Button(root, text = 'O', bd = '5', fg = getFgCol(keyDict['o']), bg = getBgCol(keyDict['o']))
        btnP = Button(root, text = 'P', bd = '5', fg = getFgCol(keyDict['p']), bg = getBgCol(keyDict['p']))
        btnA = Button(root, text = 'A', bd = '5', fg = getFgCol(keyDict['a']), bg = getBgCol(keyDict['a']))
        btnS = Button(root, text = 'S', bd = '5', fg = getFgCol(keyDict['s']), bg = getBgCol(keyDict['s']))
        btnD = Button(root, text = 'D', bd = '5', fg = getFgCol(keyDict['d']), bg = getBgCol(keyDict['d']))
        btnF = Button(root, text = 'F', bd = '5', fg = getFgCol(keyDict['f']), bg = getBgCol(keyDict['f']))
        btnG = Button(root, text = 'G', bd = '5', fg = getFgCol(keyDict['g']), bg = getBgCol(keyDict['g']))
        btnH = Button(root, text = 'H', bd = '5', fg = getFgCol(keyDict['h']), bg = getBgCol(keyDict['h']))
        btnJ = Button(root, text = 'J', bd = '5', fg = getFgCol(keyDict['j']), bg = getBgCol(keyDict['j']))
        btnK = Button(root, text = 'K', bd = '5', fg = getFgCol(keyDict['k']), bg = getBgCol(keyDict['k']))
        btnL = Button(root, text = 'L', bd = '5', fg = getFgCol(keyDict['l']), bg = getBgCol(keyDict['l']))
        btnZ = Button(root, text = 'Z', bd = '5', fg = getFgCol(keyDict['z']), bg = getBgCol(keyDict['z']))
        btnX = Button(root, text = 'X', bd = '5', fg = getFgCol(keyDict['x']), bg = getBgCol(keyDict['x']))
        btnC = Button(root, text = 'C', bd = '5', fg = getFgCol(keyDict['c']), bg = getBgCol(keyDict['c']))
        btnV = Button(root, text = 'V', bd = '5', fg = getFgCol(keyDict['v']), bg = getBgCol(keyDict['v']))
        btnB = Button(root, text = 'B', bd = '5', fg = getFgCol(keyDict['b']), bg = getBgCol(keyDict['b']))
        btnN = Button(root, text = 'N', bd = '5', fg = getFgCol(keyDict['n']), bg = getBgCol(keyDict['n']))
        btnM = Button(root, text = 'M', bd = '5', fg = getFgCol(keyDict['m']), bg = getBgCol(keyDict['m']))
        btnMinus = Button(root, text = '-', bd = '5', fg = getFgCol(keyDict['-']), bg = getBgCol(keyDict['-']))
        btnEquals = Button(root, text = '=', bd = '5', fg = getFgCol(keyDict['=']), bg = getBgCol(keyDict['=']))
        btnSqBracetOpen = Button(root, text = '[', bd = '5', fg = getFgCol(keyDict['[']), bg = getBgCol(keyDict['[']))
        btnSqBracetClose = Button(root, text = ']', bd = '5', fg = getFgCol(keyDict[']']), bg = getBgCol(keyDict[']']))
        btnBackSlash = Button(root, text = '\\', bd = '5', fg = getFgCol(keyDict['\\']), bg = getBgCol(keyDict['\\']), width=6)
        btnSemiColon = Button(root, text = ';', bd = '5', fg = getFgCol(keyDict[';']), bg = getBgCol(keyDict[';']))
        btnQuote = Button(root, text = '\'', bd = '5', fg = getFgCol(keyDict['\'']), bg = getBgCol(keyDict['\'']))
        btnComma = Button(root, text = ',', bd = '5', fg = getFgCol(keyDict[',']), bg = getBgCol(keyDict[',']))
        btnDot = Button(root, text = '.', bd = '5', fg = getFgCol(keyDict['.']), bg = getBgCol(keyDict['.']))
        btnSlash = Button(root, text = '/', bd = '5', fg = getFgCol(keyDict['/']), bg = getBgCol(keyDict['/']))
        btnEsc = Button(root, text = 'esc', bd = '5', fg = getFgCol(keyDict['esc']), bg = getBgCol(keyDict['esc']))
        btnTab = Button(root, text = 'tab', bd = '5', fg = getFgCol(keyDict['tab']), bg = getBgCol(keyDict['tab']), width=4)
        btnCaps = Button(root, text = 'caps lock', bd = '5', fg = getFgCol(keyDict['caps lock']), bg = getBgCol(keyDict['caps lock']))
        btnLShift = Button(root, text = 'shift', bd = '5', fg = getFgCol(keyDict['shift']), bg = getBgCol(keyDict['shift']), width=10)
        btnRShift = Button(root, text = 'shift', bd = '5', fg = getFgCol(keyDict['shift']), bg = getBgCol(keyDict['shift']), width=12)
        btnLCtrl = Button(root, text = 'ctrl', bd = '5', fg = getFgCol(keyDict['ctrl']), bg = getBgCol(keyDict['ctrl']))
        btnRCtrl = Button(root, text = 'ctrl', bd = '5', fg = getFgCol(keyDict['ctrl']), bg = getBgCol(keyDict['ctrl']))
        btnLAlt = Button(root, text = 'alt', bd = '5', fg = getFgCol(keyDict['alt']), bg = getBgCol(keyDict['alt']))
        btnRAlt = Button(root, text = 'alt', bd = '5', fg = getFgCol(keyDict['alt']), bg = getBgCol(keyDict['alt']))
        btnSpace = Button(root, text = 'space', bd = '5', fg = getFgCol(keyDict['space']), bg = getBgCol(keyDict['space']), width=59)
        btnEnter = Button(root, text = 'enter', bd = '5', fg = getFgCol(keyDict['enter']), bg = getBgCol(keyDict['enter']), width=8)
        btnBackspace = Button(root, text = 'backspace', bd = '5', fg = getFgCol(keyDict['backspace']), bg = getBgCol(keyDict['backspace']))
        btnInsert = Button(root, text = 'insert', bd = '5', fg = getFgCol(keyDict['insert']), bg = getBgCol(keyDict['insert']))
        btnDelete = Button(root, text = 'delete', bd = '5', fg = getFgCol(keyDict['delete']), bg = getBgCol(keyDict['delete']))

        # button positioning       
        btnEsc.place(x=10, y=10)       
        btnInsert.place(x=10 + 1.25*buttonGap, y=10)       
        btnDelete.place(x=10 + 2.8*buttonGap, y=10)     

        btnGrave.place(x=10, y=10 + buttonGap)
        btn1.place(x=10 + buttonGap, y=10 + buttonGap)
        btn2.place(x=10 + 2*buttonGap, y=10 + buttonGap)
        btn3.place(x=10 + 3*buttonGap, y=10 + buttonGap)
        btn4.place(x=10 + 4*buttonGap, y=10 + buttonGap)
        btn5.place(x=10 + 5*buttonGap, y=10 + buttonGap)
        btn6.place(x=10 + 6*buttonGap, y=10 + buttonGap)
        btn7.place(x=10 + 7*buttonGap, y=10 + buttonGap)
        btn8.place(x=10 + 8*buttonGap, y=10 + buttonGap)
        btn9.place(x=10 + 9*buttonGap, y=10 + buttonGap)
        btn0.place(x=10 + 10*buttonGap, y=10 + buttonGap)
        btnMinus.place(x=10 + 11*buttonGap, y=10 + buttonGap)
        btnEquals.place(x=10 + 12*buttonGap, y=10 + buttonGap)        
        btnBackspace.place(x=10 + 13.1*buttonGap, y=10 + buttonGap)

        btnTab.place(x=10, y=10 + 2*buttonGap)
        btnQ.place(x=35 + buttonGap, y=10 + 2*buttonGap)
        btnW.place(x=35 + 2*buttonGap, y=10 + 2*buttonGap)
        btnE.place(x=35 + 3.1*buttonGap, y=10 + 2*buttonGap)
        btnR.place(x=35 + 4.1*buttonGap, y=10 + 2*buttonGap)
        btnT.place(x=35 + 5.1*buttonGap, y=10 + 2*buttonGap)
        btnY.place(x=35 + 6.1*buttonGap, y=10 + 2*buttonGap)
        btnU.place(x=35 + 7.1*buttonGap, y=10 + 2*buttonGap)
        btnI.place(x=35 + 8.1*buttonGap, y=10 + 2*buttonGap)
        btnO.place(x=35 + 9*buttonGap, y=10 + 2*buttonGap)
        btnP.place(x=35 + 10*buttonGap, y=10 + 2*buttonGap)
        btnSqBracetOpen.place(x=35 + 11*buttonGap, y=10 + 2*buttonGap)
        btnSqBracetClose.place(x=35 + 12*buttonGap, y=10 + 2*buttonGap)
        btnBackSlash.place(x=35 + 13*buttonGap, y=10 + 2*buttonGap)

        btnCaps.place(x=10, y=10 + 3*buttonGap)
        btnA.place(x=115, y=10 + 3*buttonGap)
        btnS.place(x=115 + buttonGap, y=10 + 3*buttonGap)
        btnD.place(x=115 + 2*buttonGap, y=10 + 3*buttonGap)
        btnF.place(x=115 + 3*buttonGap, y=10 + 3*buttonGap)
        btnG.place(x=115 + 4*buttonGap, y=10 + 3*buttonGap)
        btnH.place(x=115 + 5*buttonGap, y=10 + 3*buttonGap)
        btnJ.place(x=115 + 6*buttonGap, y=10 + 3*buttonGap)
        btnK.place(x=115 + 7*buttonGap, y=10 + 3*buttonGap)
        btnL.place(x=115 + 8*buttonGap, y=10 + 3*buttonGap)
        btnSemiColon.place(x=115 + 9*buttonGap, y=10 + 3*buttonGap)
        btnQuote.place(x=115 + 10*buttonGap, y=10 + 3*buttonGap)
        btnEnter.place(x=115 + 11*buttonGap, y=10 + 3*buttonGap)

        btnLShift.place(x=10, y=10 + 4*buttonGap)
        btnZ.place(x=135, y=10 + 4*buttonGap)
        btnX.place(x=135 + buttonGap, y=10 + 4*buttonGap)
        btnC.place(x=135 + 2*buttonGap, y=10 + 4*buttonGap)
        btnV.place(x=135 + 3*buttonGap, y=10 + 4*buttonGap)
        btnB.place(x=135 + 4*buttonGap, y=10 + 4*buttonGap)
        btnN.place(x=135 + 5*buttonGap, y=10 + 4*buttonGap)
        btnM.place(x=135 + 6*buttonGap, y=10 + 4*buttonGap)
        btnComma.place(x=135 + 7*buttonGap, y=10 + 4*buttonGap)
        btnDot.place(x=135 + 8*buttonGap, y=10 + 4*buttonGap)
        btnSlash.place(x=135 + 9*buttonGap, y=10 + 4*buttonGap)
        btnRShift.place(x=135 + 10*buttonGap, y=10 + 4*buttonGap)

        btnLCtrl.place(x=10, y=10 + 5*buttonGap)
        btnLAlt.place(x=10 + 1.25*buttonGap, y=10 + 5*buttonGap)
        btnSpace.place(x=10 + 2.5*buttonGap, y=10 + 5*buttonGap)
        btnRAlt.place(x=500 + 3*buttonGap, y=10 + 5*buttonGap)
        btnRCtrl.place(x=500 + 4.2*buttonGap, y=10 + 5*buttonGap)

        mainloop()
    except Exception as e:
        print('Debug error: [001]',e)

# run at exit 
atexit.register(showHotKeyBoard)

while True:
    try:
        key = keyboard.read_key()
        if key not in escapeKeys:
            keyDict[keyboard.read_key()] += 1
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print('Debug error: [000]',e)
        showHotKeyBoard()
        break