from fastapi import FastAPI
from pathlib import Path
import pickle, sys

import trash

# Check data file is present
# data = None
# try:
#     configFile = str(Path.home())+'/GarbageReminder/trash_data.pkl'
#     with open(configFile, 'rb') as file:
#         data = pickle.load(file)
# except:
#     print('No datafile found')
#     sys.exit(1)

garbage = trash.initialize()
garbage = trash.check_garbage_day(garbage, api=True)
print(garbage)