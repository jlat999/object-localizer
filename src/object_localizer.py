class ObjectLocalizer:
    """Algorithms used for the object location estimation."""

    def __init__(self, aircraft):
        self.calibration_matrix = aircraft.get_calibration_matrix()
        self.transformation = aircraft.get_camera_transform()
        pass

    def estimate_object_location(self):
        """Estimates and returns the object absolute position."""
        x, y = 0

        return (x, y)
