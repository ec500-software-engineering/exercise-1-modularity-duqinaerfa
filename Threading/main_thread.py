import Input_Module_lkn
import Alert_module
import AiModule
import UserInterface_module
import storage
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

    storage_data = zip(bo, bp, pul)
    data_save = list(storage_data)
    stored_data = []
    for i in data_save:
        tmp = storage.storage(i)
        stored_data.append(tmp)

    key_words = ['bo', 'bp', 'pul']
    alert_sys = Alert_module.Alert()
    for i in range(3):
        for key in ['bo', 'bp', 'pul']:
            for j in stored_data:
                data_in = [j.read(key), i]
                alert_sys.Alert_for_three_categories_input(data_in)
    alert_sound = alert_sys.Alert_Output()

    UserInterface_module.getFromData(bo, bp, pul)
    UserInterface_module.getFromAlert(alert_sound)
    UserInterface_module.getFromAI(predBloodOxygen,predBloodPressure,prePulse)

    try:
        _thread.start_new_thread(storage.storage(data_save))
        _thread.start_new_thread(UserInterface_module.getFromAI(predBloodOxygen,predBloodPressure,prePulse))
        _thread.start_new_thread(UserInterface_module.getFromData(bo, bp, pul))
    except RuntimeError:
        print ("Error: unable to start thread")


if __name__ == "__main__":
    main()
