# #########################################
#  Segmentating multiple pages
#  Developed by: Tharushi Dhanushka
#  Date : 4/1/2022
###########################################

import cv2
import os
from os import listdir
import glob
import time
import sys
import json
import numpy as np
# from PIL import Image
import shape_recognize.main as SR


def build_model(is_cuda):
    net = cv2.dnn.readNet("yolov5/runs/train/exp2/weights/last.onnx")
    if is_cuda:
        print("Attempt to use CUDA")
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
    else:
        print("Running on CPU")
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    return net

INPUT_WIDTH = 640
INPUT_HEIGHT = 640
SCORE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
CONFIDENCE_THRESHOLD = 0.4

def detect(image, net):
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (INPUT_WIDTH, INPUT_HEIGHT), swapRB=True, crop=False)
    net.setInput(blob)
    preds = net.forward()
    return preds

def load_classes():
    class_list = []
    with open("model/names.names", "r") as f:
        class_list = [cname.strip() for cname in f.readlines()]
    return class_list


class_list = load_classes()


def wrap_detection(input_image, output_data):
    class_ids = []
    confidences = []
    boxes = []
    rows = output_data.shape[0]
    image_width, image_height, _ = input_image.shape
    x_factor = image_width / INPUT_WIDTH
    y_factor = image_height / INPUT_HEIGHT

    for r in range(rows):
        row = output_data[r]
        confidence = row[4]
        if confidence >= 0.4:
            classes_scores = row[5:]
            _, _, _, max_indx = cv2.minMaxLoc(classes_scores)
            class_id = max_indx[1]
            if (classes_scores[class_id] > .25):
                confidences.append(confidence)
                class_ids.append(class_id)
                x, y, w, h = row[0].item(), row[1].item(), row[2].item(), row[3].item()
                left = int((x - 0.5 * w) * x_factor)
                top = int((y - 0.5 * h) * y_factor)
                width = int(w * x_factor)
                height = int(h * y_factor)
                box = np.array([left, top, width, height])
                # print(box)
                boxes.append(box)

    # Non-Maximum Suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.25, 0.45)

    #indexes = boxes
    result_class_ids = []
    result_confidences = []
    result_boxes = []

    for i in indexes:
        result_confidences.append(confidences[i])
        result_class_ids.append(class_ids[i])
        result_boxes.append(boxes[i])
    return result_class_ids, result_confidences, result_boxes


def format_yolov5(input):
    row, col, _ = input.shape
    _max = max(col, row)
    result = np.zeros((_max, _max, 3), np.uint8)
    result[0:row, 0:col] = input
    return result


colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 0)]

is_cuda = len(sys.argv) > 1 and sys.argv[1] == "cuda"

net = build_model(is_cuda)


# rescale image
def rescaleImg(img, scale_percent=50):
    height, width, channel = img.shape

    if height > 700 or width > 1200:
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dimension = (width, height)
        resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
        return resized
    else:
        resized = img
        return resized



array =[]
path = glob.glob("img/*.jpeg")
for file in path:
    img = cv2.imread(file)
    path_list = file.split(os.sep)
    page_name = path_list[1]
    height, width, channel = img.shape
    array.append(page_name)
    array.append(width)
    print(array)

    # resize image
    input = rescaleImg(img)

    inputImage = format_yolov5(input)

    outs = detect(inputImage, net)
    class_ids, confidences, boxes = wrap_detection(inputImage, outs[0])
    print("Reading page...")

    index=0
    for (classid, confidence, box) in zip(class_ids, confidences, boxes):
            index +=1
            # color = colors[int(classid) % len(colors)]
            # rect=cv2.rectangle(input, box, color, 2)
            # cv2.rectangle(frame, (box[0], box[1] - 20), (box[0] + box[2], box[1]), color, -1)
            # cv2.putText(frame, class_list[classid], (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0))

            for index, cnt in enumerate(contours):  # take one by one segment to send text and shape recognise process
                (x, y, w, h) = cv2.boundingRect(cnt)  # find segment's bounding rectangle
                # increase 2 x and y coordination before crop image, because it crop without losing data
                x = x - 2
                y = y - 2
                w = w + 4
                h = h + 4
                crop_img = img[y:y + h, x:x + w]  # crop image using bounding rectangle
                cv2.imshow('crop', crop_img)
                cv2.waitKey(0)

            # page_height, page_width,channel = input.shape
            # x=box[0] - 2
            # y=box[1] - 2
            # h=box[2] + 4
            # w=box[3] + 4
            # crop_img = input[y:y + w, x:x + h]
            # cv2.imshow('crop', crop_img)
            # cv2.waitKey(0)



            width_crop_img, height_crop_img, channels = crop_img.shape
            if width_crop_img == 0 or height_crop_img == 0 or channels == 0:
                continue
            else:
                element_name, presentage = SR.shapeRecognizeMain(crop_img.copy)
                print(element_name)

            # Cropping elements
            new = cv2.imwrite('img/croped_img/' + str(index) + '.jpeg', crop_img)
            # PIL.Image.open(new)
            # image_sequence = new.getdata()
            # image_array = np.array(image_sequence)
            # print(image_array)

            # Generate an array
            array_output = [

                        [page_name, page_width],
                        [ [index], [box[0], box[1], box[2], box[3]],'img/croped_img/'+ str(index) + '.jpg' ]
                      # ["element_ID":index,'left': box[0],'top': box[1],'width': box[2],'height': box[3] ,"img_path":'img/croped_img/'+ str(index) + '.jpg' ]
                ]
            print(array_output)


            # clear cropped image folder
            # files = glob.glob('/img/croped_img/*.jpeg')
            # for f in files:
            #     os.remove(f)




cv2.waitKey(0)





