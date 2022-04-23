import cv2
import math
import numpy as np


def findEdgs(cnt):  # find edges of the contours
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
    return approx


def shape(c):  # find shape of the contours approximately
    length = cv2.arcLength(c, True)
    approximation = cv2.approxPolyDP(c, 0.04 * length, True)

    if len(approximation) == 3:
        shape = "triangle"
    elif len(approximation) == 4:
        (x, y, w, h) = cv2.boundingRect(approximation)
        ar = w / float(h)
        shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"

    # elif len(approx) == 5:
    #     shape = "pentagon"
    else:
        shape = "other"
    return shape, approximation


# if received a contours, then return leftmost, rightmost, topmost, bottommost edgs x and y values
def mostLRTB(cnt):
    leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
    bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
    return leftmost, rightmost, topmost, bottommost


# if received two of contours, then return FIRST CONTOUR position Related with SECOND CONTOUR
def whatIsLeft(cnt):
    # MLC1 = Most Left point of contour 1
    MLC1, MRC1, MTC1, MBC1 = mostLRTB(cnt[0])
    MLC2, MRC2, MTC2, MBC2 = mostLRTB(cnt[1])

    # blankImg = np.zeros((600, 1200, 3), np.uint8)
    # cv2.drawContours(blankImg, [cnt1], -1, (0, 255, 0), 1)
    # cv2.drawContours(blankImg, [cnt2], -1, (0, 255, 0), 1)
    # cv2.circle(blankImg, (MLC1[0], MLC1[1]), 5, (0, 0, 255), 2)
    # cv2.circle(blankImg, (MRC1[0], MLC1[1]), 5, (255, 0, 0), 2)
    # cv2.circle(blankImg, (int(abs(MLC1[0] - MRC1[0]) / 2) + MLC1[0], MLC1[1]), 5, (255, 0, 255), 2)
    # cv2.imshow("testddd", blankImg)
    # cv2.waitKey(0)

    if (abs(MLC1[0] - MRC1[0]) / 2) + MLC1[0] < (abs(MLC2[0] - MRC2[0]) / 2) + MLC2[0]:
        # return 1st parameter is left
        return 0
    else:
        # return 2nd parameter is left
        return 1


def whatIsLarge(cnt):  # find large contour of tow contours
    if cv2.contourArea(cnt[0]) > cv2.contourArea(cnt[1]):
        return 0
    else:
        return 1


# If received parent contour, set of child contours and percentage of minimum contour area, return average equal or not
def approxInnerAreaEquals(parentCnt, cnts, percentage=1):
    parentArea = cv2.contourArea(parentCnt)
    sum = 0
    for c in cnts:
        sum = sum + cv2.contourArea(c)

    avg = (parentArea * percentage) / sum
    print(avg)
    if 0.5 < avg < 1.5:
        return 1
    else:
        return 0


def pointsDistance(point1, point2):  # find distance of two points
    distance = math.sqrt((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2)
    return distance


def laegestContours(Contours):  # find largest contours of set of contours
    temp = 0
    largestCntIndex = 0
    for cntIdx, cnt in enumerate(Contours):
        if cv2.contourArea(cnt) > temp:
            temp = cv2.contourArea(cnt)
            largestCntIndex = cntIdx

    return largestCntIndex


def countInnerCtn(treeContours, treeHierarchy, parentIdx=0):
    count = 0
    ctn_idxs = []

    try:
        ctn_idx = treeHierarchy[0][parentIdx][2]

    except:
        print("Count Inner Contours Error")
        return count, ctn_idxs

    else:
        if ctn_idx == -1:
            return count, ctn_idxs
        else:
            while ctn_idx > -1:
                if (cv2.contourArea(treeContours[parentIdx])) * 0.01 < cv2.contourArea(treeContours[ctn_idx]):
                    count += 1
                    ctn_idxs.append(ctn_idx)
                    ctn_idx = treeHierarchy[0][ctn_idx][0]
                else:
                    ctn_idx = treeHierarchy[0][ctn_idx][0]

            return count, ctn_idxs


def centerOfContour(c):  # find center of contours
    M = cv2.moments(c)
    x = int(M['m10'] / M['m00'])
    y = int(M['m01'] / M['m00'])

    return x, y


def isIn(outer, inner):
    count = 0  # this count variable use for count all cnt's points are inner in hull
    for c in inner:
        dist = cv2.pointPolygonTest(outer, (c[0][0], c[0][1]), True)
        if dist > 0:  # check point is inner or outer, if inner count + 1
            count = count + 1
        else:
            continue
    if count == len(inner):  # compare length of contour and count, if same all count that contour is in the hull
        return 1
    else:
        return 0


def reSchedulechild(child_indexes, tree_contour):  # some missing child shapes are corrected and re schedule children
    re_schedule_supper_child_index = []
    for idx, data in enumerate(child_indexes):
        hull = cv2.convexHull(tree_contour[data])
        for idx2, data2 in enumerate(child_indexes):
            if data != data2:
                val = isIn(hull, tree_contour[data2])
                if val == 0:
                    continue
                else:
                    child_indexes.pop(idx2)
                    re_schedule_supper_child_index.append(data2)
            else:
                continue
    return child_indexes, re_schedule_supper_child_index


def removeSmallest(contours, hierarchy, max_value):  # find smallest contours af set contours and remove that smallest
    new_contours = []
    new_hierarchy = []

    for i, c in enumerate(contours):
        if int(cv2.contourArea(c)) > int(max_value):
            new_contours.append(c)
            new_hierarchy.append(hierarchy[0][i])
        else:
            continue
    new_hierarchy = np.array([new_hierarchy])

    return new_contours, new_hierarchy


def realNameOfElement(element_keyword):  # if received key of element, return real element name
    if element_keyword == "BTN":
        return "Button"
    elif element_keyword == "CB":
        return "Checkbox"
    elif element_keyword == "DD":
        return "Dropdown"
    elif element_keyword == "HPL":
        return "Hyperlink"
    elif element_keyword == "IMG":
        return "Image"
    elif element_keyword == "TEXT":
        return "Text Field"
    elif element_keyword == "HPL":
        return "Hyperlink"
    elif element_keyword == "PW":
        return "Password"
    elif element_keyword == "RB":
        return "Radio Button"
    elif element_keyword == "LBL":
        return "Label"


def fileCreatorForArray(array):  # create file
    with open('file.txt', 'w') as f:
        for item in array:
            f.write("%s\n" % item)
    print("success create file.txt in root folder")
    return 1


def drawText(text, img, point):  # draw text on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(text), (int(point[0]), int(point[1])), font, .4, (0, 0, 250), 1, cv2.LINE_AA)
    return 1


def drawContourIndexs(ctns, image):  # draw contours indexes
    for index, cp in enumerate(ctns):
        drawText(index, image, cp[0][0])
    return 1
