import Input_Module_lkn
import threading
import time
import Alert_module
import AiModule
import queue

def thread1 (input_queue,output_queue):
    while True:
        try:
            Input = input_queue
            if Input == 'exit':
                output_queue.put('exit')
                break
            else:
                data = Input_Module_lkn.read_data('./input_data.txt')
                if data is None:
                    print("Wrong Path!")
                    continue
                output_queue.put(data)
        except IOError:
            time.sleep(3)
    print('Thread1 Complete')


def thread2(input_queue,Alert_output_queue,AI_output_queue):
    while True:
        try:
            Input = input_queue
            if Input == 'exit':
                Alert_output_queue.put('exit')
                break
            else:
                alert_sys = Alert_module.Alert()
                for i in range(3):
                    for j in Input:
                        alert_sys.Alert_for_three_categories_input([j[i], i])

                alert_sound1, alert_sound2, alert_sound3 = alert_sys.Alert_Output()
                Alert_output_queue.put([alert_sound1, alert_sound2, alert_sound3])

                ai_sys = AiModule.AiModule()
                ai_input = list(zip(*Input))
                ai_sys.input_check(list(ai_input[0]), list(ai_input[1]), list(ai_input[2]))
                predict_bo, predict_bp, predict_pul = ai_sys.predict()
                AI_output_queue.put([predict_bo, predict_bp, predict_pul])
        except IOError:
            time.sleep(1)
    print('Thread2 Complete')


def thread3(Alert_input_queue,AI_input_queue):
    while True:
        try:
            Input = Alert_input_queue
            if Input == 'exit':
                break
            else:
                a1, a2, a3 = Input[0], Input[1], Input[2]
                if a1 != 0:
                    print("BO Alarm")
                if a2 != 0:
                    print("BP Alarm")
                if a3 != 0:
                    print("Pulse Alarm")
        except IOError:
            pass

        try:
            if Input == 'exit':
                break
            else:
                Input = AI_input_queue
                predBloodOxygen, predBloodPressure, prePulse = Input[0], Input[1], Input[2]
                print('predicted blood oxygen is: ' + str(predBloodOxygen))
                print('predicted blood pressure is: ' + str(predBloodPressure))
                print('predicted pulse is: ' + str(prePulse))
                print("")
        except IOError:
            time.sleep(1)
    print('Thread3 Complete')


if __name__ == '__main__':
    input_queue = queue.Queue()
    data_queue = queue.Queue()
    display_Alert_queue = queue.Queue()
    display_AI_queue = queue.Queue()
    thread_1 = threading.Thread(target=thread1(input_queue, data_queue))
    thread_2 = threading.Thread(target=thread2(data_queue, display_Alert_queue, display_AI_queue))
    thread_3 = threading.Thread(target=thread3(display_Alert_queue, display_AI_queue))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    input_queue.put('input_data.txt')
    time.sleep(1)
    input_queue.put('exit')
