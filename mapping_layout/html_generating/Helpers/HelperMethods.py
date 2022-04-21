import json
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32,
                              np.float64)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def object_sort(page_no, json_data_for_page, top_values, left_values):
    sort_by_top = []
    for top in top_values:
        top_val = []
        for obj in json_data_for_page:
            if json_data_for_page[obj]["top"].split("%")[0] == top:
                top_val.append({obj: json_data_for_page[obj]})

        if len(top_val) > 1:
            # start horizontally sorting
            x = 0
            y = 1
            for i in top_val:
                for j in top_val:
                    x_keys = top_val[x].keys()
                    y_keys = top_val[y].keys()
                    x_key = ""
                    y_key = ""

                    for k1 in x_keys:
                        x_key = k1
                    for k2 in y_keys:
                        y_key = k2
                    val_i = int(top_val[x].get(x_key)["left"].split("%")[0])
                    val_j = int(top_val[y].get(y_key)["left"].split("%")[0])
                    if val_i > val_j:
                        temp = top_val[x]
                        top_val[x] = top_val[y]
                        top_val[x] = temp
                x += 1
        sort_by_top.append(top_val)
    return sort_by_top


def re_format(sorted_array):
    index = 1
    arr = {}

    for sub_array in sorted_array:
        sub_arr = {}
        for obj in sub_array:
            sub_arr.update(obj)

        arr.update({"div" + str(index): sub_arr})
        index += 1
    return arr


# Adding margin top values
def margin_top_values(val):
    margin_top = 0
    if (val['type'] == "password" or val['type'] == "textarea" or val['type'] == "label" or val['type'] == "text" or
            val['type'] == "input"):
        margin_top = 0.5
    if (val['type'] == "h5" or val['type'] == "h6" or val['type'] == "p" or val['type'] == "img" or val[
        'type'] == "h1" or val['type'] == "h2" or val['type'] == "h3" or val['type'] == "h4"):
        margin_top = 1
    if (val['type'] == "a" or val['type'] == "submit" or val['type'] == "reset" or val['type'] == "dropdown" or val[
        'type'] == "button"):
        margin_top = 1.5
    return margin_top


# Set Margin for elements
def margin_adder(sorted_array):
    margin_top = 0

    for div in sorted_array:
        previous_obj = None

        before_sort = []
        for obj in div:
            keys = obj.keys()

            for key in keys:
                keys = key
            values = obj.values()

            for val in values:
                left = int(val['left'].split("%")[0])
                top = int(val['top'].split("%")[0])
                width = int(val['width'].split("%")[0])
                height = int(val['height'].split("%")[0])

                margin_left = 0
                margin_top = 0

                if (previous_obj != None):
                    margin_left = left - previous_obj[0] - previous_obj[2]
                    if (margin_left < 0):
                        margin_left = 0
                    # margin_top = top - previous_obj[1] - previous_obj[3]
                    margin_top = margin_top_values(val)

                else:
                    margin_left = left
                    if (margin_left < 0):
                        margin_left = 0
                    # margin_top = 1
                    margin_top = margin_top_values(val)

                previous_obj = [left, top, width, height]

            formatted_top = str(margin_top) + "%"
            formatted_left = str(margin_left) + "%"
            obj.get(key)["margin-top"] = formatted_top
            obj.get(key)["margin-left"] = formatted_left

            # check the element width and height and reduce if larger than expected
            if (val['type'] == 'submit' or val['type'] == 'reset' or val['type'] == 'button' or val[
                'type'] == 'dropdown'):
                if (int(val['width'].split("%")[0]) > 15):
                    obj.get(key)["width"] = "15%"
                if (int(val['height'].split("%")[0]) > 6):
                    obj.get(key)["height"] = "6%"
            if (val['type'] == 'input' or val['type'] == 'text' or val['type'] == 'password'):
                if (int(val['width'].split("%")[0]) > 25):
                    obj.get(key)["width"] = "25%"
                if (int(val['height'].split("%")[0]) > 7):
                    obj.get(key)["height"] = "7%"
            if (val['type'] == 'radio' or val['type'] == 'checkbox'):
                if (int(val['width'].split("%")[0]) > 2):
                    obj.get(key)["width"] = "2%"
                if (int(val['height'].split("%")[0]) > 3):
                    obj.get(key)["height"] = "3%"

    return sorted_array


# This function is used to find the matching arrays.
# The output will be like [5,8]
# That mean the html tag type in array 5 and 8
def match_with_elm(object):
    keys = object.keys()
    key = ""
    match = []
    for k in keys:
        key = k
    x = object.get(key)["type"]
    html_arr_1 = ['html', 'head', 'title', 'body', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img']
    html_arr_2 = ['b', 'i', 'sub', 'u', 'strong', "center"]
    html_arr_3 = ['form', 'textarea', 'textbox', 'select', 'label', 'input', 'button', "option", 'radio', 'checkbox',
                  'dropdown', 'img'
                              'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'submit', 'reset']
    html_arr_4 = ['frame', 'frameSet']
    html_arr_5 = ['li', 'a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img']
    html_arr_6 = ['br', 'hr']
    html_arr_7 = ['img', 'area', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
    html_arr_8 = ['a', 'nav', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img']
    html_arr_9 = ['ul', 'li', 'td', 'ol', 'dl', 'dd', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img']
    html_arr_10 = ['table', 'caption', 'tr', 'th', 'td', 'thead', 'tea staff', 'tbody', 'col', 'captions', 'tfooter',
                   'h1', 'h2',
                   'h3', 'h4', 'h5', 'h6', 'p', 'img']
    html_arr_11 = ['style', 'span', 'footer', 'header', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p',
                   'img']
    if x in html_arr_1:
        match.append(1)

    if x in html_arr_2:
        match.append(2)

    if x in html_arr_3:
        match.append(3)

    if x in html_arr_4:
        match.append(4)

    if x in html_arr_5:
        match.append(5)

    if x in html_arr_6:
        match.append(6)

    if x in html_arr_7:
        match.append(7)

    if x in html_arr_8:
        match.append(8)

    if x in html_arr_9:
        match.append(9)

    if x in html_arr_10:
        match.append(10)

    if x in html_arr_11:
        match.append(11)

    return match



countries =["afghanistan", "antartica", "austria","brazil", "canada", "china","denark", "fiji", "france", "germany","haiti","iceland","india","japan","jordan","kuwait","lebonon","mali","nepal","pakistan","peru","Singapore","Somalia","sri lanka","Thailand","uganda","uk","usa","venezuela","zimbabwe"]
k=0
# Dropdown option list
def DropDownOption(key_value, option_values):
    if key_value =="country":
        both_selected_non_selected = ''
        for i in range(k, k + 1):
            for item in countries:
                if option_values == item:
                    option = "<option selected>" + item + "</option>"
                else:
                    option = "<option>" + item + "</option>"
                both_selected_non_selected += option
        return both_selected_non_selected

    if key_value =="gender":
        return "<option>--Select--</option><option>Male</option><option>Female</option>"
    else:
        return "<option>Option 1</option><option>Option 2</option><option>Option 3</option>"