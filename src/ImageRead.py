# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:29:39 2022

@author: jlalctar
"""

import pathlib
from object_detector import ObjectDetector
path = pathlib.Path("./baseddades/")

images = list(path.glob("*"))

for i in images:
    img = str(i.absolute())
    detector = ObjectDetector(img)
    detector.detect_object


    
    