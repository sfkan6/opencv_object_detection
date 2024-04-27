# To run, move the files one directory higher
from object_detection import Thresher, HSVThresher, Detector
from frame_selector import FrameSelector
import cv2, numpy as np


class MyHSVThresher(HSVThresher):
    '''
    Thresher:
        Converts an image to a threshold image
        threshold_image = cv.threshold(img, 0, 255, cv.THRESH_OTSU)

    HSVThresher:
        Converts the image to a threshold image, leaving only the transmitted hsv ranges
    '''

    def get_enhanced_threshold_image(self, threshold_image):
        kernel = np.ones((3, 3), np.uint8)
        threshold_image = cv2.morphologyEx(
            threshold_image, cv2.MORPH_OPEN, kernel, iterations=4
        )
        threshold_image = cv2.morphologyEx(
            threshold_image, cv2.MORPH_DILATE, kernel, iterations=4
        )

        return threshold_image


def main():
    '''
    Find all the red objects and get these frames:

        1) Vertical:
            wh_min <= frame.width / frame.height <= wh_max:

        2) The height is more than 10% of the image

        3) All frames nested by x will be merged

        4) The size of the resulting frames will be increased by 3 pixels wide and 6 pixels high

        5) The x coordinates will be sorted in ascending order

    Thresher:
        image -> threshold_image_with_hsv_range -> contours -> frames

    FrameSelector:
        frames -> filtered_frames -> increased_frames -> sorted_frames
    '''
    image = cv2.imread('test.jpg')
    height, width = image.shape[:2]
    selector = FrameSelector(height, width)

    red_hsv_ranges = [
        [(0, 150, 30), (15, 255, 255)],
        [(175, 0, 30), (180, 255, 255)]
    ]
    thresher = MyHSVThresher(red_hsv_ranges)
    # thresher = Thresher()

    # save threshold_image
    # img = thresher.get_finished_image(image)
    # cv2.imwrite('threshold_image.jpg', img)

    frames = Detector(thresher, selector).get_frames_by_image(image)
    print(len(frames))
    print(frames)

    # save images
    # images = Detector(thresher, selector).get_frame_images(image)
    # for i in range(len(images)):
    #     cv2.imwrite(f'{i}.jpg', images[i])



main()
