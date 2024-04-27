import numpy as np
from .frame_selection import Frame


class ImageCutter:
    def __init__(self, image):
        self._image = np.array(image)

    @property
    def image(self):
        return self._image.copy()

    def get_images_by_frames(self, frames):
        return [self.get_image_by_frame(frame) for frame in frames]

    def get_images_by_rectangles(self, rectangles):
        return [self.get_image_by_rectangle(*rectangle) for rectangle in rectangles]

    def get_image_by_frame(self, frame: Frame):
        return self.get_image_by_rectangle(*frame.bounding_rect)

    def get_image_by_rectangle(self, x, y, width, height):
        return self.get_image_by_coordinates(x, y, x + width, y + height)

    def get_image_by_coordinates(self, x0, y0, x1, y1):
        return self.image[y0:y1, x0:x1]
