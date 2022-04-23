import shape_recognize.lib.api as API
import numpy as np
import cv2
import random as rng


class Elements:

    def __init__(self):
        self.BTN = []
        self.CB = []
        self.DD = []
        self.HPL = []
        self.IMG = []
        self.TEXT = []
        self.PRGF = []
        self.PW = []
        self.RB = []
        self.LBL = []
        self.CNN = []

    def addBTN(self, value):
        self.BTN.append(value)

    def addCB(self, value):
        self.CB.append(value)

    def addDD(self, value):
        self.DD.append(value)

    def addHPL(self, value):
        self.HPL.append(value)

    def addIMG(self, value):
        self.IMG.append(value)

    def addTEXT(self, value):
        self.TEXT.append(value)

    def addPRGF(self, value):
        self.PRGF.append(value)

    def addPW(self, value):
        self.PW.append(value)

    def addRB(self, value):
        self.RB.append(value)

    def addLBL(self, value):
        self.LBL.append(value)

    def addCNN(self, description, name_of_data, data):
        self.CNN.append([description, name_of_data, data])


class Features:

    def __init__(self, E, EC, TC, TH):
        self.E = E
        self.EC = EC
        self.TC = TC
        self.TH = TH
        # self.count = None
        # self.child_ctn_idxs = None

        self.LCI = 0
        # LCI = Largest Contour Index

        if len(EC) > 1:
            self.LCI = API.laegestContours(EC)

        # PCI = Parent's Contours Index in Tree Contours'
        self.PCI = 0

        for i, c in enumerate(self.TC):
            if np.array_equal(self.EC[self.LCI], c):
                self.PCI = i

        self.count, self.child_ctn_idxs = API.countInnerCtn(self.TC, self.TH, self.PCI)

        # RE SCHEDULE CHILD INDEXES AFTER COUNT CHILD INDEXES
        child_indexes, re_schedule_supper_child_index = API.reSchedulechild(self.child_ctn_idxs, self.TC)

        self.count = len(child_indexes)
        self.child_ctn_idxs = child_indexes
        self.re_schedule_supper_child_index = re_schedule_supper_child_index

        # blank_image = np.zeros((600, 1200, 3), np.uint8)
        # cv2.drawContours(blank_image, self.TC, -1, (0, 255, 0), 1)
        #
        # for i in self.child_ctn_idxs:
        #     cv2.drawContours(blank_image, self.TC, i, (255, 255, 0), 1)
        #     cv2.imshow("test =", blank_image)
        #     cv2.waitKey(0)


    def main(self):
        self.externalShape()

        if self.count == 1:
            # print("count == 1")
            self.E.addBTN(5)
            self.E.addRB(5)
            self.E.addLBL(5)
            self.innerCnt1Shape()
            self.supperInnerCnt1Shape()
            self.errorSolvedCnt1()

            # cv2.drawContours(img, contoursRT, -1, (255, 0, 0), 1)
            # cv2.imshow("image", img)
            # cv2.waitKey(0)

        elif self.count == 2:
            # print("count == 2")
            self.E.addDD(5)
            self.E.addHPL(5)
            self.E.addTEXT(5)
            self.E.addPRGF(5)
            self.innerCnt2Shape()
            self.contourCount2Special()

        elif self.count == 3:
            # print("count == 3")
            self.E.addIMG(5)
            self.innerCnt3Shape()
            self.errorSolvedCnt3()

        elif self.count == 4:
            # print("count == 4")
            self.E.addCB(5)
            self.E.addPW(5)
            self.imageSpecial()
            self.innerCnt4Shape()
            self.checkBoxSpecial()
            self.passwordSpecial()

        else:
            # print("count =", self.count)
            # check special features of count 4
            self.imageSpecial()
            self.innerCnt4Shape()
            self.checkBoxSpecial()
            self.passwordSpecial()

        return self.E

    def externalShape(self):
        shape, approx = API.shape(self.EC[self.LCI])

        if shape == "rectangle":
            # print("externalShape == rectangle")
            self.E.addBTN(5)
            self.E.addCB(5)
            self.E.addDD(5)
            self.E.addHPL(5)
            self.E.addIMG(5)
            self.E.addTEXT(5)
            self.E.addPRGF(5)
            self.E.addPW(5)
            self.E.addRB(5)
            self.E.addLBL(5)
            return self.E

        elif shape == "square":
            # print("externalShape == square")

            self.E.addCB(5)
            self.E.addIMG(5)
            self.E.addRB(5)
            return self.E

        else:
            return self.E

    def innerCnt1Shape(self):
        for cntIdx in self.child_ctn_idxs:
            child_shape, points = API.shape(self.TC[cntIdx])
            if child_shape == "rectangle":
                # print("innerCnt1Shape == rectangle")
                self.E.addBTN(10)
                self.E.addRB(10)
                self.E.addLBL(10)
            elif child_shape == "square":
                # print("innerCnt1Shape == square")

                self.E.addRB(10)
        return self.E

    def innerCnt2Shape(self):
        for cntIdx in self.child_ctn_idxs:
            child_shape, points = API.shape(self.TC[cntIdx])
            if child_shape == "triangle":
                # print("innerCnt2Shape == triangle")
                self.E.addPRGF(2.5)
            elif child_shape == "rectangle":
                # print("innerCnt2Shape == rectangle")
                self.E.addDD(2.5)
                self.E.addHPL(2.5)
                self.E.addTEXT(2.5)
                self.E.addPRGF(2.5)
            elif child_shape == "square":
                # print("innerCnt2Shape == square")
                self.E.addDD(2.5)
                self.E.addTEXT(2.5)
            else:
                # print("innerCnt2Shape == else")
                self.E.addHPL(2.5)
                self.E.addIMG(2.5)
                self.E.addPRGF(2.5)

        return self.E

    def innerCnt3Shape(self):
        for cntIdx in self.child_ctn_idxs:
            child_shape, points = API.shape(self.TC[cntIdx])
            if child_shape == "triangle":
                self.E.addIMG(3)
            elif child_shape == "rectangle" or child_shape == "square":
                self.E.addIMG(3)
            else:
                self.E.addIMG(3)
        return self.E

    def innerCnt4Shape(self):
        for cntIdx in self.child_ctn_idxs:
            child_shape, points = API.shape(self.TC[cntIdx])
            if child_shape == "triangle":
                self.E.addCB(2.5)
            elif child_shape == "rectangle" or child_shape == "square":
                self.E.addPW(2.5)
            else:
                self.E.addIMG(2.5)
        return self.E

    def supperInnerCnt1Shape(self):
        for cntIdx in self.child_ctn_idxs:
            super_inner_count, super_inner_ctn_idxs = API.countInnerCtn(self.TC, self.TH, cntIdx)

            if super_inner_count == 1:
                child_shape, points = API.shape(self.TC[super_inner_ctn_idxs[0]])
                if child_shape == "rectangle" or child_shape == "square":
                    self.E.addBTN(80)
                    return self.E
                else:
                    self.E.addRB(80)
                    return self.E
            elif super_inner_count == 0:
                self.E.addLBL(80)
                return self.E
            else:
                return self.E

    def contourCount2Special(self):

        left_cnt_index = 0
        right_cnt_index = 1
        c1 = self.TC[self.child_ctn_idxs[left_cnt_index]]
        c2 = self.TC[self.child_ctn_idxs[right_cnt_index]]

        left = API.whatIsLeft([c1, c2])
        large = API.whatIsLarge([c1, c2])

        if left == large:
            self.E.addDD(5)
            self.E.addHPL(5)
            self.dropdownSpecial(right_cnt_index)
        else:
            self.E.addTEXT(5)
            self.E.addPRGF(5)
            self.labelSpecial(left_cnt_index)

        # MLP = Most left point of parent
        # MLC1 = Most Left point of child 1
        MLP, MRP, MTP, MBP = API.mostLRTB(self.TC[self.PCI])
        MLC1, MRC1, MTC1, MBC1 = API.mostLRTB(c1)
        MLC2, MRC2, MTC2, MBC2 = API.mostLRTB(c2)
        parent_width = abs(MLP[0] - MRP[0])

        self.paragraphSpecial(parent_width, MLC1, MLC2)
        self.hyperlinkSpecial(parent_width, MRC1, MRC2)

        return self.E

    def dropdownSpecial(self, right_cnt_index):

        grand_child_count, grand_child_index = API.countInnerCtn(self.TC, self.TH, self.child_ctn_idxs[right_cnt_index])
        if len(grand_child_index) == 1:
            GCS, GCA = API.shape(self.TC[grand_child_index[0]])
            if GCS == "triangle":
                self.E.addDD(75)
            else:
                return self.E

    def labelSpecial(self, left_cnt_index):
        grand_child_count, grand_child_index = API.countInnerCtn(self.TC, self.TH, self.child_ctn_idxs[left_cnt_index])
        if grand_child_count == 0:
            self.E.addTEXT(74)
            return self.E
        else:
            return self.E

    def paragraphSpecial(self, parent_width, MLC1, MLC2):

        if parent_width * 0.1 > abs(MLC1[0] - MLC2[0]):
            self.E.addPRGF(75)
            return self.E
        else:
            return self.E

    def hyperlinkSpecial(self, parent_width, MRC1, MRC2):

        if parent_width * 0.1 > abs(MRC1[0] - MRC2[0]):
            self.E.addHPL(75)
            return self.E
        else:
            return self.E

    def imageSpecial(self):
        for cntIdx in self.child_ctn_idxs:
            super_child_count, super_child_idxs = API.countInnerCtn(self.TC, self.TH, cntIdx)
            if super_child_count == 1:

                child_shape, points = API.shape(self.TC[super_child_idxs[0]])
                if child_shape == "other":
                    self.E.addIMG(70)
                else:
                    continue
            else:
                continue
        return self.E

    def checkBoxSpecial(self):
        x, y = API.centerOfContour(self.TC[self.PCI])

        for cntIdx in self.child_ctn_idxs:
            shape, edges = API.shape(self.TC[cntIdx])
            for point in edges:
                distance = API.pointsDistance([x, y], point[0])
                if distance < 20:
                    self.E.addCB(20)
                else:
                    continue
        return self.E

    def passwordSpecial(self):
        x, y = API.centerOfContour(self.TC[self.PCI])
        # img = np.zeros((600, 1200, 3), np.uint8)
        # cv2.circle(img, (x, y), 3, (0, 255, 255), -1)

        MLP, MRP, MTP, MBP = API.mostLRTB(self.TC[self.PCI])

        for cntIdx in self.child_ctn_idxs:
            x2, y2 = API.centerOfContour(self.TC[cntIdx])
            if abs(y - y2) < (abs(MTP[1]-MBP[1])*0.1):
                self.E.addPW(20)
            else:
                continue
        return self.E

    def errorSolvedCnt1(self):
        # error identification solve
        if len(self.re_schedule_supper_child_index) == 1:
            s, a = API.shape(self.TC[self.re_schedule_supper_child_index[0]])
            if s == "rectangle" or s == "rectangle":
                self.E.addBTN(100)
            else:
                self.E.addRB(80)

    def errorSolvedCnt3(self):
        # error identification solve
        if len(self.re_schedule_supper_child_index) == 1:
            s, a = API.shape(self.TC[self.re_schedule_supper_child_index[0]])
            if s == "other":
                self.E.addIMG(80)
            else:
                self.E.addIMG(60)
