import os
import json

class Secrets():

    def __init__(self):
        if os.path.isfile('secrets.json'):
            with open('secrets.json','r') as jsonFile:
                data = json.load(jsonFile)
                self.cerebro_long_eegs_mat_folder = data['EEG_folder']
        else:
            self.cerebro_long_eegs_mat_folder = 'EEG_Folder'