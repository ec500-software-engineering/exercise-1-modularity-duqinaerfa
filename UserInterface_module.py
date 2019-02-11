#It's the I/O documentation for the User_Interface_system
#Qinmei Du
#User Interface
class userInterface():
    def __init__(self):
        self.bo = []
        self.bp = []
        self.pul = []
        self.boalert = []
        self.bpalert = []
        self.pulalert = []
        self.operation = []

    def getFromAlert(self, boalert, bpalert, pulalert):
        """
        Get_data_from_alert_sys:format: three flags from alert sys output to trigger alert display
        """
        self.boalert = boalert
        self.bpalert = bpalert
        self.pulalert = pulalert

    def getFromData(self, bo, bp, pul):
        """
        Get_data_from_data_base: format:(double value, int type)
        """
        self.bo = bo
        self.bp = bp
        self.pul = pul

    def getFromUser(self, operation):
        """
        Get_data_from_user: format: boolean control from user. Such as turn on, turn off user log in information
        """
        self.operation = operation

    def sendToShow(self):
        """
        send input to electron device to show on the screen
        """
        send_data = {
            self
        }
        print(send_data)
        return send_data

