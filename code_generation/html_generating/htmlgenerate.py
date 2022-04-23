import json
import code_generation.html_generating.layout_methods as layout_methods
import zipfile
import os
import webbrowser
import glob


# remove output files from the folder
def removeOutputDataInHTML():

    files = glob.glob('E:/Personal/New folder/CodeSquad/code_generation/html_generating/HtmlOutput/webpages/*')
    for f in files:
        os.remove(f)
    return 1
removeOutputDataInHTML()


def generateHtml():

    # Start reading the input.json file
    with open('E:/Personal/New folder/CodeSquad/code_generation/InputFiles/mapping_layouts.json') as f:
        data = json.load(f)  # load the file
    pages = len(data)  # calculate the number of pages
    reformated_dic = {}

    # Start reading the input.json file

    for page in data:  # Iterate through all pages
        top_values = []
        left_values = []
        for obj in data[page]:  # Go through all abjects and gat TOP and LEFT values. Then add to the array
            top = data[page][obj]["top"].split("%")[0]
            left = data[page][obj]["left"].split("%")[0]

            if not top in top_values:
                top_values.append(top)
            if not left in left_values:
                left_values.append(left)
        top_values.sort()  # Sort the top valus arrays
        left_values.sort()

        sorted_object_array = layout_methods.sort(page, data[page], top_values,
                                                  left_values)  # Call to sort accrdingly left and top vales
        x = layout_methods.add_margin(sorted_object_array)  # To add the margin top and margin left

        x = layout_methods.add_div(sorted_object_array)  # This shoud be updated to group objects
        reformated_dic.update({page: x})

        try:
            with open("../InputFiles/formated.json", 'w+') as fs:
                y = json.dumps(reformated_dic, indent=2, sort_keys=False, cls=layout_methods.NumpyEncoder)
                fs.write(y)

        except Exception as e:
            print("Failed to write to file, Reson : " + str(e))
            pass

        print("Done for page {}======".format(page))

    # Write page names to newList array
    newList = []

    # load json file
    with open('E:/Personal/New folder/CodeSquad/code_generation/InputFiles/formated.json') as json_data:
        loaded_json = json.load(json_data)

    # HTML code generation
    for i in range(0, len(loaded_json) + 1):
        for key in loaded_json.keys():
            newList.append(key)

            html = ''
            # html tags read
            div_key = ''
            for z in loaded_json[newList[i]]:
                # print("z:", z)
                add_divs_panel = ''
                html_tag = ''
                groupId = ''

                for x in loaded_json[newList[i]][z]:
                    attribute = ''
                    # tag's attribute read
                    w = ''
                    style_all = "style=\""
                    subattributes = ''

                    if groupId == "":
                        groupId = loaded_json[newList[i]][z][x]['groupId']
                        html_tag += "<span>\n"
                        for y in loaded_json[newList[i]][z][x]:
                            # define array for dropdown options
                            dropdownoptions = []
                            # subattributes = ''
                            if type(loaded_json[newList[i]][z][x][y]) is dict:
                                # read sub attributes
                                for xy in range(0, len(loaded_json[newList[i]][z][x][y])):
                                    dropdownoptions = loaded_json[newList[i]][z][x][y]['values'][xy]
                                    # subattributes += "\n<" + loaded_json[newList[i]][z][x][y][
                                    #     'type'] + ">" + dropdownoptions + "</" + \
                                    #                  loaded_json[newList[i]][z][x][y]['type'] + ">"
                                    subattributes = layout_methods.DropDownOption(loaded_json[newList[i]][z][x]['text'], loaded_json[newList[i]][z][x][y]['text'])

                            else:
                                if y == "top" or y == "left" or y == "groupId":
                                    # if y == "top" or y == "left" or y == "groupId" or y == "margin-top" or y == "margin-left":
                                    continue

                                styles = ''
                                if y == "width" or y == "height" or y == "margin-top" or y == "margin-left" or y == "align":
                                    # if y == "width" or y == "height":

                                    if y == "width":
                                        # hide the dropdown width for dropdown responsiveness
                                        if (loaded_json[newList[i]][z][x]['type'] == 'dropdown' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'radio' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'checkbox' or
                                                loaded_json[newList[i]][z][x]['type'] == 'textarea' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'text' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'password' or
                                                loaded_json[newList[i]][z][x]['type'] == 'submit' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'reset' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'button' or
                                                loaded_json[newList[i]][z][x]['type'] == 'h1' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'h2' or loaded_json[newList[i]][z][x]['type'] == 'h3' or
                                                loaded_json[newList[i]][z][x]['type'] == 'h4' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'h5' or loaded_json[newList[i]][z][x]['type'] == 'h6'):
                                            continue

                                        if (loaded_json[newList[i]][z][x]['type'] == 'p'):
                                            if (int(loaded_json[newList[i]][z][x]['width'].split("%")[0]) < 60):
                                                style_all = style_all + "display: inline;"

                                    if y == "height":
                                        if (loaded_json[newList[i]][z][x]['type'] == 'p' or loaded_json[newList[i]][z][x][
                                            'type'] == 'radio' or loaded_json[newList[i]][z][x]['type'] == 'checkbox'):
                                            continue

                                    style_all = style_all + y + ":" + loaded_json[newList[i]][z][x][y] + ";"

                                else:
                                    # remove p tag attributes (type, text..)
                                    if loaded_json[newList[i]][z][x]['type'] == 'p' or loaded_json[newList[i]][z][x][
                                        'type'] == 'img':
                                        continue
                                    attribute += "" + y + "=" "\"" + loaded_json[newList[i]][z][x][y] + "\" "

                        style_all = style_all + "\" "
                        attributeWithStyles = attribute + style_all

                        html_tag += "<" + layout_methods.input_password(
                            loaded_json[newList[i]][z][x][
                                'type']) + " " + attributeWithStyles + layout_methods.addClass(
                            loaded_json[newList[i]][z][x]['type']) + ">" + subattributes + "   " + loaded_json[newList[i]][z][x][
                                        'text'] + "</" + layout_methods.input_password(
                            loaded_json[newList[i]][z][x]['type']) + ">" + "\n"
                        if x == list(loaded_json[newList[i]][z].keys())[-1]:
                            html_tag += "</span>\n"
                    elif groupId != loaded_json[newList[i]][z][x]['groupId']:
                        html_tag += "</span>\n<span>\n"
                        groupId = loaded_json[newList[i]][z][x]['groupId']



                        for y in loaded_json[newList[i]][z][x]:
                            # define array for dropdown options
                            dropdownoptions = []
                            # subattributes = ''
                            if type(loaded_json[newList[i]][z][x][y]) is dict:
                                # read sub attributes
                                for xy in range(0, len(loaded_json[newList[i]][z][x][y])):
                                    dropdownoptions = loaded_json[newList[i]][z][x][y]['values'][xy]
                                    subattributes = layout_methods.DropDownOption(loaded_json[newList[i]][z][x]['text'], loaded_json[newList[i]][z][x][y]['text'])

                            else:
                                if y == "top" or y == "left" or y == "groupId":
                                    # if y == "top" or y == "left" or y == "groupId" or y == "margin-top" or y == "margin-left":
                                    continue

                                styles = ''
                                if y == "width" or y == "height" or y == "margin-top" or y == "margin-left" or y == "align":
                                    # if y == "width" or y == "height":

                                    if y == "width":
                                        # hide the dropdown width for dropdown responsiveness
                                        if (loaded_json[newList[i]][z][x]['type'] == 'dropdown' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'radio' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'checkbox' or
                                                loaded_json[newList[i]][z][x]['type'] == 'textarea' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'text' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'password' or
                                                loaded_json[newList[i]][z][x]['type'] == 'submit' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'reset' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'button' or
                                                loaded_json[newList[i]][z][x]['type'] == 'h1' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'h2' or loaded_json[newList[i]][z][x]['type'] == 'h3' or
                                                loaded_json[newList[i]][z][x]['type'] == 'h4' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'h5' or loaded_json[newList[i]][z][x]['type'] == 'h6'):
                                            continue

                                        if (loaded_json[newList[i]][z][x]['type'] == 'p'):
                                            if (int(loaded_json[newList[i]][z][x]['width'].split("%")[0]) < 60):
                                                style_all = style_all + "display: inline;"

                                    if y == "height":
                                        if (loaded_json[newList[i]][z][x]['type'] == 'p' or loaded_json[newList[i]][z][x][
                                            'type'] == 'radio' or loaded_json[newList[i]][z][x]['type'] == 'checkbox'):
                                            continue

                                    style_all = style_all + y + ":" + loaded_json[newList[i]][z][x][y] + ";"

                                else:
                                    # remove p tag attributes (type, text..)
                                    if loaded_json[newList[i]][z][x]['type'] == 'p' or loaded_json[newList[i]][z][x][
                                        'type'] == 'img':
                                        continue
                                    attribute += "" + y + "=" "\"" + loaded_json[newList[i]][z][x][y] + "\" "

                        style_all = style_all + "\" "
                        attributeWithStyles = attribute + style_all

                        html_tag += "<" + layout_methods.input_password(
                            loaded_json[newList[i]][z][x][
                                'type']) + " " + attributeWithStyles + layout_methods.addClass(
                            loaded_json[newList[i]][z][x]['type']) + ">" + subattributes + "   " + loaded_json[newList[i]][z][x][
                                        'text'] + "</" + layout_methods.input_password(
                            loaded_json[newList[i]][z][x]['type']) + ">" + "\n"
                        if x == list(loaded_json[newList[i]][z].keys())[-1]:
                            html_tag += "</span>\n"
                    else:
                        for y in loaded_json[newList[i]][z][x]:
                            # define array for dropdown options
                            dropdownoptions = []
                            # subattributes = ''
                            if type(loaded_json[newList[i]][z][x][y]) is dict:
                                # read sub attributes
                                for xy in range(0, len(loaded_json[newList[i]][z][x][y])):
                                    dropdownoptions = loaded_json[newList[i]][z][x][y]['values'][xy]
                                    # subattributes += "\n<" + loaded_json[newList[i]][z][x][y][
                                    #     'type'] + ">" + dropdownoptions + "</" + \
                                    #                  loaded_json[newList[i]][z][x][y]['type'] + ">"
                                    subattributes = layout_methods.DropDownOption(loaded_json[newList[i]][z][x]['text'], loaded_json[newList[i]][z][x][y]['text'])

                            else:
                                if y == "top" or y == "left" or y == "groupId":
                                    # if y == "top" or y == "left" or y == "groupId" or y == "margin-top" or y == "margin-left":
                                    continue

                                styles = ''
                                if y == "width" or y == "height" or y == "margin-top" or y == "margin-left" or y == "align":
                                    # if y == "width" or y == "height":

                                    if y == "width":
                                        # hide the dropdown width for dropdown responsiveness
                                        if (loaded_json[newList[i]][z][x]['type'] == 'dropdown' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'radio' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'checkbox' or
                                                loaded_json[newList[i]][z][x]['type'] == 'textarea' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'text' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'password' or
                                                loaded_json[newList[i]][z][x]['type'] == 'submit' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'reset' or loaded_json[newList[i]][z][x][
                                                    'type'] == 'button' or
                                                loaded_json[newList[i]][z][x]['type'] == 'h1' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'h2' or loaded_json[newList[i]][z][x]['type'] == 'h3' or
                                                loaded_json[newList[i]][z][x]['type'] == 'h4' or
                                                loaded_json[newList[i]][z][x][
                                                    'type'] == 'h5' or loaded_json[newList[i]][z][x]['type'] == 'h6'):
                                            continue

                                        if (loaded_json[newList[i]][z][x]['type'] == 'p'):
                                            if (int(loaded_json[newList[i]][z][x]['width'].split("%")[0]) < 60):
                                                style_all = style_all + "display: inline;"

                                    if y == "height":
                                        if (loaded_json[newList[i]][z][x]['type'] == 'p' or loaded_json[newList[i]][z][x][
                                            'type'] == 'radio' or loaded_json[newList[i]][z][x]['type'] == 'checkbox'):
                                            continue

                                    style_all = style_all + y + ":" + loaded_json[newList[i]][z][x][y] + ";"

                                else:
                                    # remove p tag attributes (type, text..)
                                    if loaded_json[newList[i]][z][x]['type'] == 'p' or loaded_json[newList[i]][z][x][
                                        'type'] == 'img':
                                        continue
                                    attribute += "" + y + "=" "\"" + loaded_json[newList[i]][z][x][y] + "\" "

                        style_all = style_all + "\" "
                        attributeWithStyles = attribute + style_all

                        html_tag += "<" + layout_methods.input_password(
                            loaded_json[newList[i]][z][x][
                                'type']) + " " + attributeWithStyles + layout_methods.addClass(
                            loaded_json[newList[i]][z][x]['type']) + ">" + subattributes + "   " + loaded_json[newList[i]][z][x][
                                        'text'] + "</" + layout_methods.input_password(
                            loaded_json[newList[i]][z][x]['type']) + ">" + "\n"
                        if x == list(loaded_json[newList[i]][z].keys())[-1]:
                            html_tag += "</span>\n"

                # Add NavBar or Divs
                if (next(iter(loaded_json[newList[i]])) == "div1"):
                    if (next(iter(loaded_json[newList[i]][z])) == "HPL-1"):
                        div_key += "<nav class=\"navbar navbar-light bg-light\">\n" + html_tag + "</nav>\n"
                    else:
                        div_key += "<div class=""\"media\">\n" + html_tag + "</div>\n"

                # div_key += "<div class=""\"media\">\n" + html_tag + "</div>\n"
                add_divs_panel += layout_methods.formSetUp(
                    loaded_json[newList[i]][z][x]['type']) + div_key + layout_methods.formSetDown(
                    loaded_json[newList[i]][z][x]['type'])

            html += "<html>\n<head>\n" + layout_methods.CSS_Scripts() + "\n</head>\n<body " + layout_methods.BodyStyles() + ">\n" + layout_methods.formSetUp(
                loaded_json[newList[i]][z][x]['type']) + div_key + layout_methods.formSetDown(
                loaded_json[newList[i]][z][x]['type']) + "</body>\n</html>"
            # open('Test' + newList[i] + '.html', 'w').write(html)

            open("E:/Personal/New folder/CodeSquad/code_generation/html_generating/HtmlOutput/webpages/" + newList[i] + '.html', 'w').write(html)

        try:
            with open("E:/Personal/New folder/CodeSquad/code_generation/html_generating/HtmlOutput/webpages/" + newList[i] + '.html', 'w').write(
                    html) as fs:
                y = json.dumps(reformated_dic, indent=2, sort_keys=False, cls=layout_methods.NumpyEncoder)
                fs.write(y)
        except Exception as e:
            pass

    # Change path to reflect file location
    filename = "E:/Personal/New folder/CodeSquad/code_generation/html_generating/HtmlOutput/webpages/" + newList[0] + '.html'
    webbrowser.open_new_tab(filename)


    def dir_of_zip(path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
    zipf = zipfile.ZipFile('webpages.zip', 'w', zipfile.ZIP_DEFLATED)
    dir_of_zip("E:/Personal/New folder/CodeSquad/code_generation/html_generating/HtmlOutput/webpages/", zipf)
    zipf.close()
