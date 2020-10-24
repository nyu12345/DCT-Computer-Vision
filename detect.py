import apriltag
import cv2
import os
import numpy as np


# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# slide a window across the image
def reader(detector, img, file_name):
    tag_list = []
    global img2

    for y in range(0, img.shape[0], 350):
        for x in range(0, img.shape[1], 350):
            result, img2 = detector.detect(img[y:y + 450, x:x + 450], return_image=True)
            print(result)
            if (len(result) != 0) and all(result) not in tag_list:
                tag_list.append(result)
                cv2.imwrite("Outputs/"+file_name+".output.jpg", img2)
    return tag_list


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detector = apriltag.Detector()
    directory = "data/Track 10-22/"
    file = directory+"60_2.png"
    print(file)
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    tag_list = reader(detector, img, file)
    print(tag_list)
    cap.release()
    cv2.destroyAllWindows()
