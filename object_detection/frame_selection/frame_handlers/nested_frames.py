from ..frame_handling import FrameHandler


class NestedFrameHandler(FrameHandler):
    def get_frames(self, frames):
        i = 0
        while i < len(frames) - 1:
            if frames[i].is_nested_by_x(frames[i + 1]):
                frames[i].union_frames(frames[i + 1])
                frames.pop(i + 1)
            else:
                i += 1
        return frames
