from shape_recognize.model import *
import cv2
import os
import glob


def elementPreProcessing(img):  # precessing cropped image to recognize shape
    canny = cv2.Canny(img, 120, 120)
    kernel = np.ones((3, 3))
    closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

    _, contoursRE, hierarchyRE = cv2.findContours(closing, cv2.RETR_EXTERNAL,
                                                  cv2.CHAIN_APPROX_SIMPLE)  # find external contour
    _, contoursRT, hierarchyRT = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find tree contours

    blankImg = np.zeros((600, 600, 3), np.uint8)
    cv2.drawContours(blankImg, contoursRT, -1, (255, 255, 0), 1)
    cv2.imshow("test", blankImg)
    cv2.waitKey(0)

    return contoursRE, hierarchyRE, contoursRT, hierarchyRT


def shapeRecognizeMain(image):
    # cv2.imshow("image_segment",image)
    # cv2.waitKey(0)

    EC, EH, TC, TH = elementPreProcessing(image)

    # print(EC)
    # print(EH)
    # print(TC)
    # print(TH)

    E = Elements()  # create elements object to store data of shape recognise process
    F = Features(E, EC, TC, TH)  # create features object and send data to feature extraction
    F.main()  # call features object main method

    # print(np.sum(E.BTN))

    # create total data array to analysing data
    total = [["BTN", np.sum(E.BTN)], ["CB", np.sum(E.CB)], ["DD", np.sum(E.DD)], ["HPL", np.sum(E.HPL)],
             ["IMG", np.sum(E.IMG)], ["TEXT", np.sum(E.TEXT)], ["HPLINK", np.sum(E.HPLINK)], ["PW", np.sum(E.PW)],
             ["RB", np.sum(E.RB)], ["LBL", np.sum(E.LBL)]]

    # total = sorted(total, key=lambda total_entry: total_entry[1])
    # print(total)
    # totalReverse = sorted(total, key=lambda total_entry: total_entry[1], reverse=True)
    # for ele in totalReverse:
    #     print(ele)

    ElementMax = max(total, key=lambda total_entry: total_entry[
        1])  # get max values of weighted data and get that element data

    if int(ElementMax[1]) == 0 or int(ElementMax[1]) > 120:  # if element max have 0 or grater than 120, skip it
        return 0, "none"
    else:

        # print("Identified Shape => : ", API.realNameOfElement(ElementMax[0]), "-", int(ElementMax[1]), "%")

        return ElementMax[0], ElementMax[1]


def removeOutputData():  # remove old output data to create new output data
    files = glob.glob('D:/Coder\'s Cafe/shape_recognize/output/*')
    for f in files:
        os.remove(f)
    return 1


def drawShapeRecognizeOutput(element_name, img_copy, cnt, page_number, percentage):
    # this function use for draw shape recognized output details and
    # write output images details in path{shape_recognize/output}

    # ___ start draw percentage of identification of image shape ______
    # percentage_img = img_copy.copy()
    # API.drawText(str(percentage), percentage_img, [cnt[0][0][0], cnt[0][0][1]])
    # cv2.imwrite('shape_recognize/output/' + str(page_number) + "percentage.jpg", percentage_img)
    # ___ end draw percentage of identification of image shape ______

    API.drawText(element_name, img_copy, [cnt[0][0][0], cnt[0][0][1]])
    # cv2.imshow(str(page_number), img_copy) # show image of output in open window

    cv2.imwrite('shape_recognize/output/' + str(page_number) + ".jpg", img_copy)
    # print("identified shapes . .  created output image in path shape_recognize/output")
    # cv2.waitKey(0)
    return 1

