import os
os.system("python predict.py -c config_license_plates.json -i dayride_type1_001.mp4#t=37.jpg")

os.system("python test.py -i cut/dayride_type1_001.mp4#t=37.jpg")

