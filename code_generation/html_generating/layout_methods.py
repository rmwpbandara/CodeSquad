import json
import numpy as np




def sort(page_no, json_data_for_page, top_values, left_values):
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


def add_div(sorted_array):
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
def top_margin(val):
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
def add_margin(sorted_array):
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
                    margin_top = top_margin(val)

                else:
                    margin_left = left
                    if (margin_left < 0):
                        margin_left = 0
                    # margin_top = 1
                    margin_top = top_margin(val)

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



# setup form when receive form elements -- form starting tag
def formSetUp(tag):
    if (tag == "input") or (tag == "radio") or (tag == "checkbox") or (tag == "reset") or (tag == "submit") or (
            tag == "textarea") or (tag == "text") or (tag == "password"):
        return "<div>\n<form class=\"form-inline\">"
    else:
        return ""


# form ending tag
def formSetDown(tag):
    if (tag == "input") or (tag == "radio") or (tag == "checkbox") or (tag == "reset") or (tag == "submit") or (
            tag == "textarea") or (tag == "text") or (tag == "password"):
        return "</form>\n</div>"
    else:
        return ""


# if input type=password set tag type=input // type=dropdown set tag type=select
def input_password(tag):
    if (tag == "password") or (tag == "radio") or (tag == "checkbox") or (tag == "text"):
        return "input"
    elif (tag == "submit") or (tag == "reset"):
        return "button"
    elif (tag == "dropdown"):
        return "select"
    else:
        return tag



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


# body Styles
def BodyStyles():
    bStyles = 'style=\"margin:20px;background-color: #e6ffff;background-image: url(../bg-image.jpg);background-size: cover\"'
    return bStyles


# CSS, Script
def CSS_Scripts():
    links = '<title>Sample Web Page</title>\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>\n<link rel="stylesheet" href="Styles/Styles.css">'
    return links


# if tag is "label" - then enter <br> tag
# def br_tag(tag):
#     if (tag == "button") or (tag == "textarea") or (tag == "submit"):
#         br = "<br><br>"
#         return br
#     elif (tag == "radio") or (tag == "checkbox"):
#         return "<br>"
#     else:
#         return ""


# add attributes to tags(class)
def addClass(tag):
    if (tag == "submit"):
        return "class=\"btn btn-success text-capitalize\""
    elif (tag == "reset"):
        return "class=\"btn btn-danger text-capitalize\""
    if (tag == "button"):
        return "class=\"btn btn-secondary text-capitalize\""
    elif (tag == "a"):
        return "class=\"nav-link text-capitalize\""
    elif (tag == "dropdown"):
        return "class=\"btn btn-info dropdown-toggle form-control text-capitalize\""
    elif (tag == "img"):
        return "class=\"img-fluid\" src=\"../test.jpg\""
    elif (tag == "p"):
        return "class =\"text-justify text-dark\""
    elif (tag == "text") or (tag == "password") or (tag == "textarea"):
        return "class =\"form-control\""
    elif (tag == "label"):
        return "class =\"form-check-label text-capitalize\""
    elif (tag == "checkbox"):
        return "class =\"form-check-input text-capitalize\""
    elif (tag == "radio"):
        return "class =\"form-check-input text-capitalize\""
    elif (tag == "h1" or tag == "h2" or tag == "h3" or tag == "h4" or tag == "h5" or tag == "h6"):
        return "class =\"text-dark\""
    else:
        return ""



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