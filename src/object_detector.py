class ObjectDetector:
    """Algorithms used for the object detection."""

    def __init__(self, aircraft):
        self.aircraft = aircraft
        pass

    def preprocess_image(self):
        frame = self.aircraft.get_next_frame()
        pass

    def detect_object(self):
        pass

    def draw_bounding_box(self, position, frame):
        """Sets the bounding box of the detected object.

        input:
            - position (tuple(float, float)): Position of 
            the upper left corner of the bounding box.
            - frame (): Image that needs the bounding box.
        output:
            - boxed_frame (): image with the bounding box.
        """
        pass