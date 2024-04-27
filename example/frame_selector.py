from object_detection import (
    FrameHandler,
    Selector,
    NestedFrameHandler,
    AspectRatioHandler,
    RectanglePositionHandler,
    Sorter
)


class FrameIncreaser(FrameHandler):
    '''
    Increases the boundaries
    '''
    def __init__(self, increase_in_height, increase_in_width):
        self.increase_in_height = increase_in_height
        self.increase_in_width = increase_in_width

    def get_frames(self, frames):
        return [
            frame.get_increase_frame(self.increase_in_height, self.increase_in_height)
            for frame in frames
        ]


class VerticalPositionFilter(RectanglePositionHandler):
    '''
    Leaves only vertical rectangles
    '''
    def __init__(self, hw_min=1, hw_max=8, wh_min=2, wh_max=5):
        super().__init__(hw_min, hw_max, wh_min, wh_max)

    def is_correct_frame(self, frame):
        if self.is_vertical_rectangle(frame):
            return True
        return False


class HeightRatioFilter(AspectRatioHandler):
    '''
    Leaves only such rectangles:
        frame.height / image_height > n_height
    '''
    def __init__(self, image_height, image_width, n_width=0.1, n_height=0.1):
        super().__init__(image_height, image_width, n_width, n_height)

    def is_correct_frame(self, frame):
        if self.is_height_more_n_percent_of_image(frame):
            return True
        return False


class FrameSelector(Selector):
    def __init__(self, height, width, increase_in_height=6, increase_in_width=3):
        frame_filters = [
            VerticalPositionFilter(),
            HeightRatioFilter(height, width),
            NestedFrameHandler(),
            FrameIncreaser(increase_in_height, increase_in_width),
            Sorter(),
        ]
        super().__init__(frame_filters)


