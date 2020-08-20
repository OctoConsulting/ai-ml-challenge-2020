import os
import os.path

from os import path

basepath = 'C:/Users/meredith.lee/Documents/GitHub/GSA-AI/submissions/OctoConsulting_Submission/backend/testdata/finished'

f = open(os.path.join(basepath, "finished.txt"), "w+")
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)) & entry.endswith('.txt') != True:
        f.write(entry)
        print (entry)