# To run, move the files one directory higher
from object_detection import HSVThresher
import cv2


def main():
    image = cv2.imread('test.jpg')

    red_hsv_ranges = [
        [(0, 150, 30), (15, 255, 255)],
        [(175, 0, 30), (180, 255, 255)]
    ]
    threshold_image = HSVThresher(red_hsv_ranges).get_threshold_image(image)
    cv2.imwrite('threshold_image.jpg', threshold_image)


if __name__ == '__main__':
    main()
