import pathlib
import cv2
from filtro_mc_class_nf import od

path = pathlib.Path("./baseddades/")

images = list(path.glob("*"))

for i in images:
    img = str(i.absolute())
    image = cv2.imread(img)
    cv2.imshow('image',image)
    cv2.waitKey(0)

    detector = od(img)
    print(detector.filtcanny)
    detector.filtmask

    
    