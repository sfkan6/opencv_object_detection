import cv2


class Frame:
    def __init__(self, x, y, width, height):
        self.set_frame(x, y, width, height)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return f"({self.x}, {self.y}, {self.width}, {self.height})"

    @property
    def bounding_rect(self):
        return [self.x, self.y, self.width, self.height]

    @property
    def area(self):
        return self.width * self.height

    def get_start_and_end_points(self):
        return (self.x, self.y), (self.x + self.width, self.y + self.height)

    def union_frames(self, frame):
        self.set_frame(*self.get_union_frame_by_frame(frame).bounding_rect)

    def get_union_frame_by_frame(self, frame):
        x = min(self.x, frame.x)
        y = min(self.y, frame.y)
        w = max(self.x + self.width, frame.x + frame.width) - x
        h = max(self.y + self.height, frame.y + frame.height) - y
        return self.__class__(x, y, w, h)

    def set_frame(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_increase_frame(self, increase_in_height, increase_in_width):
        return self.__class__(
            max(0, self.x - increase_in_width // 2),
            max(0, self.y - increase_in_height // 2),
            self.width + increase_in_width // 2,
            self.height + increase_in_height // 2,
        )

    def is_nested_by_x(self, frame):
        if self.x <= frame.x and self.x + self.width >= frame.x + frame.width:
            return True
        return False

    @classmethod
    def create_by_contour(cls, contour):
        return cls(*cv2.boundingRect(contour))
