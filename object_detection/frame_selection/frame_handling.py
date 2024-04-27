


class FrameHandler:
    def get_frames(self, frames):
        return [frame for frame in frames if self.is_correct_frame(frame)]

    def is_correct_frame(self, frame):
        if frame:
            return True
        return False

