import cv2
import glob

dir_path = "data/sample-files"

for file_name in glob.glob(dir_path + "/*"):
    file = cv2.imread(file_name, 0)
    resized = cv2.resize(file, (100, 100))
    cv2.imwrite(file_name, resized)
