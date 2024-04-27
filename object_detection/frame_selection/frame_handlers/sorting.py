from ..frame_handling import FrameHandler


class Sorter(FrameHandler):
    def get_frames(self, frames):
        return sorted(frames, key=lambda frame: frame.x)
