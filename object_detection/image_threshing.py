import cv2
import numpy as np
from .frame_selection import Frame


class Thresher:
    def get_finished_image(self, image):
        threshold_image = self.get_threshold_image(image)
        return self.get_enhanced_threshold_image(threshold_image)

    def get_threshold_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold_image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
        return threshold_image

    def get_enhanced_threshold_image(self, threshold_image):
        kernel = np.ones((3, 3), np.uint8)
        threshold_image = cv2.morphologyEx(
            threshold_image, cv2.MORPH_CLOSE, kernel, iterations=3
        )
        threshold_image = cv2.morphologyEx(
            threshold_image, cv2.MORPH_OPEN, kernel, iterations=1
        )
        return threshold_image

    def get_frames_by_threshold_image(self, threshold_image):
        contours = self.get_contours_by_threshold_image(threshold_image)
        return [Frame.create_by_contour(contour) for contour in contours]

    def get_contours_by_threshold_image(self, threshold_image):
        contours, _ = cv2.findContours(
            threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        return contours


class HSVThresher(Thresher):
    def __init__(self, hsv_ranges: list):
        self.hsv_ranges = hsv_ranges

    def get_threshold_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, w, _ = image.shape
        mask = np.zeros((h, w), np.uint8)
        for hsv_range in self.hsv_ranges:
            mask += cv2.inRange(image.copy(), *hsv_range)
        return mask

    def get_enhanced_threshold_image(self, threshold_image):
        kernel = np.ones((3, 3), np.uint8)
        threshold_image = cv2.morphologyEx(
            threshold_image, cv2.MORPH_OPEN, kernel, iterations=3
        )
        return threshold_image
