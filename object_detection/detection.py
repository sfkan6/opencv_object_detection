from .image_threshing import Thresher
from .frame_selection import Selector
from .image_cutter import ImageCutter


class Detector:
    def __init__(self, thresher: Thresher, selector: Selector):
        self.thresher = thresher
        self.selector = selector

    def get_frames_by_image(self, image):
        threshold_image = self.thresher.get_finished_image(image)
        frames = self.thresher.get_frames_by_threshold_image(threshold_image)
        return self.selector.get_processed_frames(frames)

    def get_frame_images(self, image):
        frames = self.get_frames_by_image(image)
        return ImageCutter(image).get_images_by_frames(frames)
