from ..frame_handling import FrameHandler


class AspectRatioHandler(FrameHandler):
    def __init__(self, image_height, image_width, n_width=0.1, n_height=0.1):
        self.image_height = image_height
        self.image_width = image_width
        self.n_height = n_height
        self.n_width = n_width

    def is_correct_frame(self, frame):
        if self.is_more_n_percent_of_image(frame):
            return True
        return False

    def is_more_n_percent_of_image(self, frame):
        if self.is_width_more_n_percent_of_image(
            frame
        ) and self.is_height_more_n_percent_of_image(frame):
            return True
        return False

    def is_width_more_n_percent_of_image(self, frame):
        if self.n_width <= frame.width / self.image_width:
            return True
        return False

    def is_height_more_n_percent_of_image(self, frame):
        if self.n_height <= frame.height / self.image_height:
            return True
        return False
