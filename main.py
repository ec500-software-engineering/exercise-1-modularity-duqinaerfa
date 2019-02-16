import Input_Module_lkn
import storage
import Alert_module
import AiModule
import UserInterface_module

"""
Input
"""
Input_bo=Input_Module_lkn.read_data('./examplebo.txt')
Input_bp=Input_Module_lkn.read_data('./examplebp.txt')
Input_pulse=Input_Module_lkn.read_data('./examplepul.txt')

UserInterface_module.getFromData(Input_bo, Input_bp, Input_pulse)

"""
Store
"""
storage_data=zip(Input_bo,Input_bp,Input_pulse)
data_save=list(storage_data)
stored_data = []
for i in data_save:
	tmp = storage.storage(i)
	stored_data.append(tmp)

"""
Alert
"""
key_words=['bo','bp','pul']
alert_sys = Alert_module.Alert()
for i in range(3):
	for key in ['bo','bp','pul']:
		for j in stored_data:
			data_in = [j.read(key),i]
			alert_sys.Alert_for_three_categories_input(data_in)
alert_sound = alert_sys.Alert_Output()
UserInterface_module.getFromAlert(alert_sound)
"""
AI
"""
ai_sys = AiModule.AiModule()

for j in stored_data:
	ai_sys.input_check(Input_bo,Input_bp,Input_pulse)

predict_bo,predict_bp,predict_pul=ai_sys.predict()

"""
UI
"""
UserInterface_module.getFromAI(predict_bo,predict_bp,predict_pul)