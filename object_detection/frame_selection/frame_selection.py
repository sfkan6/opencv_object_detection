class Selector:
    def __init__(self, frame_filters):
        self.frame_filters = frame_filters

    def get_processed_frames(self, frames):
        for frame_filter in self.frame_filters:
            frames = frame_filter.get_frames(frames)
        return frames
