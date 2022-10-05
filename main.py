import keyboard

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
}
keyDict[keyboard.read_key()] += 1

print(keyDict)

# from tkinter import *

# root = Tk()
# root.title("hot-key-board")
# root.geometry("550x220")

# btnQ = Button(root, text = 'Q', bd = '5')
# btnW = Button(root, text = 'W', bd = '5')
# btnE = Button(root, text = 'E', bd = '5')
# btnR = Button(root, text = 'R', bd = '5')
# btnT = Button(root, text = 'T', bd = '5')
# btnY = Button(root, text = 'Y', bd = '5')
# btnU = Button(root, text = 'U', bd = '5')
# btnI = Button(root, text = 'I', bd = '5')
# btnO = Button(root, text = 'O', bd = '5')
# btnP = Button(root, text = 'P', bd = '5')
# btnA = Button(root, text = 'A', bd = '5')
# btnS = Button(root, text = 'S', bd = '5')
# btnD = Button(root, text = 'D', bd = '5')
# btnF = Button(root, text = 'F', bd = '5')
# btnG = Button(root, text = 'G', bd = '5')
# btnH = Button(root, text = 'H', bd = '5')
# btnJ = Button(root, text = 'J', bd = '5')
# btnK = Button(root, text = 'K', bd = '5')
# btnL = Button(root, text = 'L', bd = '5')
# btnZ = Button(root, text = 'Z', bd = '5')
# btnX = Button(root, text = 'X', bd = '5')
# btnC = Button(root, text = 'C', bd = '5')
# btnV = Button(root, text = 'V', bd = '5')
# btnB = Button(root, text = 'B', bd = '5')
# btnN = Button(root, text = 'N', bd = '5')
# btnM = Button(root, text = 'M', bd = '5')

# btnQ.place(x=10, y=10)
# btnW.place(x=60, y=10)
# btnE.place(x=110, y=10)
# btnR.place(x=160, y=10)
# btnT.place(x=210, y=10)
# btnY.place(x=260, y=10)
# btnU.place(x=310, y=10)
# btnI.place(x=360, y=10)
# btnO.place(x=410, y=10)
# btnP.place(x=460, y=10)
# btnA.place(x=35, y=60)
# btnS.place(x=95, y=60)
# btnD.place(x=145, y=60)
# btnF.place(x=195, y=60)
# btnG.place(x=245, y=60)
# btnH.place(x=295, y=60)
# btnJ.place(x=345, y=60)
# btnK.place(x=395, y=60)
# btnL.place(x=445, y=60)
# btnZ.place(x=60, y=110)
# btnX.place(x=110, y=110)
# btnC.place(x=160, y=110)
# btnV.place(x=210, y=110)
# btnB.place(x=260, y=110)
# btnN.place(x=310, y=110)
# btnM.place(x=360, y=110)

# mainloop()