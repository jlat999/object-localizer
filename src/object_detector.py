import cv2 as cv
import numpy as np


class ObjectDetector:
    """Algorithms used for the object detection."""

    def __init__(self, aircraft):
        self.aircraft = aircraft
        pass

    def preprocess_image(self, frame):
        """Filters the image only leaving certain tones f
        of white.

        input:
            - frame (np.array): Image that needs pre-processing.
        output:
            - frame_result (np.array): Preprocessed image.
        """

        # Convert BGR to HSV
        frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # Threshold of white in HSV space
        pure_white_hsv = np.array([0, 0, 210])
        pale_gray_hsv = np.array([255, 15, 255])

        # Create and use the mask
        mask = cv.inRange(frame_hsv, pure_white_hsv, pale_gray_hsv)
        frame_masked_hsv = cv.bitwise_and(frame_hsv, frame_hsv, mask=mask)
        # Return to BGR format
        frame_result = cv.cvtColor(frame_masked_hsv, cv.COLOR_HSV2BGR)

        return frame_result

    def detect_object(self):
        """Routine that gets a frame, preprocesses it
        detects the contours and plots them.

        input:
            -
        output:
            -
        """
        frame = self.aircraft.get_next_frame()
        processed_frame = self.preprocess_image(frame)

        # Change frame to gray for the findContours algorithm
        frame_gray = cv.cvtColor(processed_frame, cv.COLOR_BGR2GRAY)
        contours, _ = cv.findContours(frame_gray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        self.draw_bounding_box(contours, frame)

    def draw_bounding_box(self, positions, frame):
        """Sets the bounding box of the detected object.

        input:
            - position (np.array): Position of
            the upper left corner of the bounding box.
            - frame (np.array): Image that needs the bounding box.
        output:
            - frame_boxed (np.array): image with the bounding box.
        """

        frame_boxed = cv.drawContours(frame, positions, 0, (0, 255, 0), 3)
        cv.imshow("frame_boxed", frame_boxed)
        cv.waitKey(0)

        return frame_boxed
