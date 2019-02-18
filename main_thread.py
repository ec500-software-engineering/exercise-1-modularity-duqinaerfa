import Input_Module_lkn
import Alert_module
import AiModule
import UserInterface_module
import storage_thread
import _thread

def test_func():
    main()

def main():
    bo = Input_Module_lkn.read_data('./examplebo.txt')
    bp = Input_Module_lkn.read_data('./examplebp.txt')
    pul = Input_Module_lkn.read_data('./examplepul.txt')

    ai = AiModule.AiModule()
    ai.input_check(bo, bp, pul)
    predBloodOxygen, predBloodPressure, prePulse = ai.predict()

    alt = Alert_module.Alert()
    for k in range(len(bo)):
        boi = bo[k], 0
        bpi = bp[k], 1
        puli = pul[k], 2
        alt.Alert_for_three_categories_input(boi)
        alt.Alert_for_three_categories_input(bpi)
        alt.Alert_for_three_categories_input(puli)
        alt.Alert_Output()

    UserInterface_module.getFromData(bo, bp, pul)
    UserInterface_module.getFromAlert(alt.Alert_Output())
    UserInterface_module.getFromAI(predBloodOxygen,predBloodPressure,prePulse)

    try:
        _thread.start_new_thread(storage_thread.storage_thread, (bo, bp, pul))
        _thread.start_new_thread(UserInterface_module.getFromAI, (predBloodOxygen,predBloodPressure,prePulse))
        _thread.start_new_thread(UserInterface_module.getFromData, (bo, bp, pul))
    except RuntimeError:
        print ("Error: unable to start thread")


if __name__ == "__main__":
    main()
