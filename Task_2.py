import numpy as np
import os

folder = "Data/wearable-device-dataset-from-induced-stress-and-structured-exercise-sessions-1.0.1/Wearable_Dataset/AEROBIC/f01/"  # <-- change this

signals = ["ACC", "BVP", "EDA", "HR", "IBI", "tags", "TEMP"]

data = {}

for sig in signals:
    filename = os.path.join(folder, f"{sig}.csv")
    data[f"f01_{sig}"] = np.loadtxt(filename, delimiter=",", dtype=str)

#f01_ACC = data["f01_ACC"]
#print(f01_ACC)

for key in data:
    if key != "f01_tags":
        data[key][1:] = data[key][1:].astype(float)
        #print(f"{key}: {data[key].shape}", data[key][:5])
