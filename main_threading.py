from AiModule import AiModule as AI
import UserInterface_module
import Input_Module_lkn as I
from Alert_module import Alert
from queue import Queue
import threading
import time

# from storage import storage as St
def Input(BoQinput):
    while True:
        #input
        I.rand_input(BoQinput)
        time.sleep(2)

def middle(BoQinput, BoQoutput):
    while True:

        if not BoQinput.empty():
            value = BoQinput.get_nowait()
            bo = value[0]
            bp = value[1]
            pul = value[2]
            #AI
            A = AI()
            A.input_check(bo, bp, pul)
            predBloodOxygen, predBloodPressure, prePulse = A.predict()
            # Alert
            Alt = Alert()
            boi = bo, 0
            bpi = bp, 1
            puli = pul, 2
            boa = Alt.Alert_for_three_categories_input(boi)
            bpa = Alt.Alert_for_three_categories_input(bpi)
            pula = Alt.Alert_for_three_categories_input(puli)
            BoQoutput.put_nowait(value)
            time.sleep(2)

def Output(BoQoutput):
    while True:
        #Interface
        if not BoQoutput.empty():
            value = BoQoutput.get_nowait()
            bo = value[0]
            bp = value[1]
            pul = value[2]
            print("Blood Oxygen:%f\nBlood presure:%f\nPulse:%f\n" % (bo,bp,pul))
            U = UserInterface_module()
            U.getFromData(bo,bp,pul)
            time.sleep(2)

if __name__ == '__main__':
    BoQinput = Queue()
    BoQoutput = Queue()
    t1 = threading.Thread(target= Input, args= (BoQinput,))
    t2 = threading.Thread(target= middle, args= (BoQinput, BoQoutput,))
    t3 = threading.Thread(target= Output, args= (BoQoutput,))
    t1.start()
    t2.start()
    t3.start()