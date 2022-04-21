def elementPreProcessing(img):  # precessing cropped image to recognize shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img_blur = cv2.medianBlur(gray, 1).astype('uint8')
    # cv2.imshow("crop img", img_blur)
    # cv2.waitKey(0)


    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    canny = cv2.Canny(img, 120, 120)
    kernel = np.ones((3, 3))
    closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("test-shape",thresh)
    cv2.waitKey(0)
    _, contoursRE, hierarchyRE = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    _, contoursRT, hierarchyRT = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contoursRE, hierarchyRE, contoursRT, hierarchyRT
