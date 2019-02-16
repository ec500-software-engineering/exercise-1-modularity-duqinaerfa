#It's the I/O documentation for the User_Interface_system
#Qinmei Du
#User Interface
def getFromData(bo, bp, pul):
    """
    Get_data_from_data_base: format:(double value, int type)
    """
    print ("The BO, BP, PUL is")
    print (bo,bp, pul)

def getFromUser(operation):
    """
    Get_data_from_user: format: boolean control from user. Such as turn on, turn off user log in information
    """
    print (operation)

def getFromAlert(alert_number):
    if alert_number == 0:
        print("Everything is fine")
    elif alert_number == 1:
        print("BO Alert!")
    elif alert_number == 2:
        print("BP Alert!")
    elif alert_number == 3:
        print("PUL Alert!")

def getFromAI(predBloodOxygen, predBloodPressure, prePulse):
    print('predicted blood oxygen is: ' + str(predBloodOxygen))
    print('predicted blood pressure is: ' + str(predBloodPressure))
    print('predicted pulse is: ' + str(prePulse))