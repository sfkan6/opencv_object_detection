from ..frame_handling import FrameHandler


class RectanglePositionHandler(FrameHandler):
    def __init__(self, hw_min=1, hw_max=8, wh_min=2, wh_max=5):
        self.hw_min = hw_min
        self.hw_max = hw_max
        self.wh_min = wh_min
        self.wh_max = wh_max

    def is_correct_frame(self, frame):
        if self.is_horizontal_rectangle(frame):
            return True
        return False

    def is_vertical_rectangle(self, frame):
        if self.hw_min <= frame.height / frame.width <= self.hw_max:
            return True
        return False

    def is_horizontal_rectangle(self, frame):
        if self.wh_min <= frame.width / frame.height <= self.wh_max:
            return True
        return False
