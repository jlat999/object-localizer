class Aircraft:
    """Contains the transform matrices and sensor data."""

    def __init__(self):
        """Initialize calibration matrix or any data we need."""
        self.camera_calibration_matrix = []
        self.transform_matrix = []
        pass

    def get_calibration_matrix(self):
        """Returns the camera calibration matrix."""

        return self.camera_calibration_matrix

    def get_transform_matrix(self):
        """Returns the camera transform matrix."""

        return self.transform_matrix

    def get_next_frame(self):
        pass
