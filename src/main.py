import logging
from object_detector import ObjectDetector
from object_localizer import ObjectLocalizer
from aircraft import Aircraft

def main():
    uav = Aircraft()
    detector = ObjectDetector(uav)
    detector.detect_object()


if __name__ == "__main__":
    main()
