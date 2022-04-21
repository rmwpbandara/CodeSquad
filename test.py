# ###############################################################################################
# #   Developed by: Tharushi Dhanushka
# #   Date        : 4/1/2022
# #   Final       : Segmenting Single page
# ###############################################################################################
import cv2
import time
import sys
import glob
import json
import numpy as np
import os
from os import listdir





def build_model(is_cuda):
    net = cv2.dnn.readNet("yolov5/runs/train/exp2/weights/last.onnx")
    if is_cuda:
        print("Attempty to use CUDA")
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


def format_yolov5(frame):
    row, col, _ = frame.shape
    _max = max(col, row)
    result = np.zeros((_max, _max, 3), np.uint8)
    result[0:row, 0:col] = frame
    return result


colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 0)]

is_cuda = len(sys.argv) > 1 and sys.argv[1] == "cuda"

net = build_model(is_cuda)



# def run():
#     path = "img/croped_img"
#     os.remove("img/croped_img")
#     for filename in os.listdir(path):
#         img = Image.open(path + '\\' + filename)
#         clrs = img.getcolors()
#         print
#         filename, len(clrs)
#         if len(clrs) == 1:
#             os.remove(path + '\\' + filename)

    # all_page_data = []
    # print(file)
    # images = file.split(',')
    # print(images)
    # for page_number, img in enumerate(images):
    #     page_name = img
    #     img = cv2.imread("img/" + img)

#input image
# imdir = 'img'
# ext = ['png', 'jpg', 'jpeg']
# files = []
# [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]
# img = [cv2.imread(file) for file in files]



img = cv2.imread('img/dfn.jpeg')

# rescale image
def rescaleImg(img, scale_percent=15):
    height, width, channel = img.shape

    print('height: ', height)
    print('width:  ', width)
    print('channel:', channel)
    if height > 700 or width > 1200:
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dimension = (width, height)
        resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
        return resized
    else:
        resized = img
        return resized


# resize image
frame = rescaleImg(img)
inputImage = format_yolov5(frame)
outs = detect(inputImage, net)
class_ids, confidences, boxes = wrap_detection(inputImage, outs[0])


count=0
for (classid, confidence, box) in zip(class_ids, confidences, boxes):
        count +=1
        color = colors[int(classid) % len(colors)]
        rect=cv2.rectangle(frame, box, color, 2)
        #cv2.imshow("rect", rect)
        #print(count)
        # cv2.rectangle(frame, (box[0], box[1] - 20), (box[0] + box[2], box[1]), color, -1)
        # cv2.putText(frame, class_list[classid], (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0))

        page_height, page_width,channel = frame.shape
        x=box[0] - 2
        y=box[1] - 2
        h=box[2] + 4
        w=box[3] + 4
        crop_img = frame[y:y + w, x:x + h]
        # cv2.imshow("crop_img", crop_img)
        new = cv2.imwrite('img/croped_img/' + str(count) + '.jpeg', crop_img)
        # print('widget ID:', count, 'page_height',page_height, 'page_width',page_width, 'left:', box[0], 'top:', box[1], 'width:', box[2], 'height:', box[3] ,  'img/croped_img/'+ str(count) + '.jpg')

        array={

            'page_height': page_height,
            'page_width':page_width,
            'element': [    {"element_ID":count,'left': box[0],'top': box[1],'width': box[2],'height': box[3] ,"img_path":'img/croped_img/'+ str(count) + '.jpg' }]

        }

        # print(array_output)
        page_name='home'

        array_output = [

                [page_name, page_width],
                [ [count], [box[0], box[1], box[2], box[3]],'img/croped_img/'+ str(count) + '.jpg' ]

        ]
        print(array_output)
cv2.imshow("output", frame)
cv2.waitKey(0)

