import cv2
import numpy as np
import shape_recognize.lib.api as API
import shape_recognize.main as SHAPE_RECOGNIZE
import sys

def run(file):
    all_page_data = []

    images = file.split(',')
    for page_number, img in enumerate(images):
        page_name = img

        img = cv2.imread("input/" + img)  # get file name from browser
        page_height, page_width, channels1 = img.shape
        if page_height > 700 or page_width > 1200:
            percentage = (760 / page_height)
            img = cv2.resize(img, (0, 0), fx=percentage, fy=percentage)
        img_copy = img.copy()
        height, width, channels = img.shape

        canny = cv2.Canny(img, ((height + width) * 0.1), 100)  # apply canny edge detection
        kernel = np.ones((5, 5))  # use (5 , 5) kernel for dilate
        dilation = cv2.dilate(canny, kernel, iterations=1)  # dilate image

        _, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                  cv2.CHAIN_APPROX_SIMPLE)  # find external contour in dilated image
        contours, hierarchy = API.removeSmallest(contours, hierarchy,
                                                 (height * width) * 0.001)  # remove smallest contours

        page_data = []  # create list for append data to send mapping and layouts
        for index, cnt in enumerate(contours):  # take one by one segment to send text and shape recognise process
            (x, y, w, h) = cv2.boundingRect(cnt)  # find segment's bounding rectangle
            # increase 2 x and y coordination before crop image, because it crop without losing data
            x = x - 2
            y = y - 2
            w = w + 4
            h = h + 4
            crop_img = img[y:y + h, x:x + w]  # crop image using bounding rectangle
            # cv2.imshow('crop', crop_img)
            # cv2.waitKey(0)

            width_crop, height_crop, channels_crop = crop_img.shape  # find width and height copped image

            if width_crop == 0 or height_crop == 0 or channels_crop == 0:  # check image can zero values
                continue
            else:
                element_name, percentage = SHAPE_RECOGNIZE.shapeRecognizeMain(crop_img.copy())  # call shape recognize main method

                if element_name == 0:
                    continue
                else:
                    print(element_name)
                    page_data.append([[element_name,"HPL-1"], [x, y, w, h]])
                    # page_data.append([[element_name], [x, y], [x + w, y], [x + w, y + h], [x, y + h]])
                    # SHAPE_RECOGNIZE.drawShapeRecognizeOutput(element_name, img_copy, cnt, img, percentage)  #

        all_page_data.append([[page_name,page_width], page_data])  # append all pages data to all page array
        # all_page_data.append([[width, height], [page_name], [page_data]])  # append all pages data to all page array

    print("--------------------------------------")
    print("Success Shape Recognize and Text Recognize")

    print(all_page_data)

    return 1


if __name__ == "__main__":

    # if there is an argument, use it. Otherwise use default file (h1.jpg)
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "Profile1.jpg"
    print('[INFO] start processing file: ' + file)

    # execute main process
    run(file)

