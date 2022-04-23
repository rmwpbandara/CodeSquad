from mapping_and_layout.shapes1 import input_array

def mappingOnePage(all_elements):
    for element in all_elements:
        element_name = element[0][1].split('-')
        element[0][1] =element_name[0]

    # add bottom right coordinates
    for element in all_elements:
        right_x_coordinate = element[1][0] + element[1][2]
        bottom_y_coordinate = element[1][1] + element[1][3]
        element[1].append(right_x_coordinate)
        element[1].append(bottom_y_coordinate)

    # print(all_elements)
    sorted_list = []
    # store x and y separately
    list_x = []
    list_y = []

    # separate x and y values from all elements to find max x and y
    for element in all_elements:
        list_x.append(element[1][4])
        list_y.append(element[1][5])

    # print("list_x :", list_x)
    # print("list_y :", list_y)

    #find maximum x value
    max_x_index = 0
    for n in range(0, len(list_x) - 1):
        if (list_x[n + 1]) > (list_x[max_x_index]):
            max_x_index = n + 1
        max_list_x = list_x[max_x_index]

    # print("max_x_index :", max_x_index)
    # print("max_list_x : ", max_list_x)

    #finding maximum y value
    max_y_index = 0
    for n in range(0, len(list_y) - 1):
        if (list_y[n + 1]) > (list_y[max_y_index]):
            max_y_index = n + 1
        max_list_y = list_y[max_y_index]

    # print("max_y_index :", max_y_index)
    # print("max_list_y : ", max_list_y)
    # print("ymax:",max_list_y)

    # sorting all elements according to the y value
    def swap(one, two):
        temp = all_elements[one]
        all_elements[one] = all_elements[two]
        all_elements[two] = temp

    for n in range(0, len(all_elements)):
        max = n
        for m in range(n + 1, len(all_elements)):
            if ((all_elements[m][1][1]) < (all_elements[max][1][1])):
                max = m
        swap(n, max)
        sorted_list.append(all_elements[n])

    # print("sorted_list_y :", sorted_list)

    # sorting all elements according to the x value

    diff_list = []

    for n in range(0, len(sorted_list) - 1):
        diff = sorted_list[n][1][5] - sorted_list[n + 1][1][1]
        diff_list.append(diff)

    # print("diff_list :", diff_list)

    adj_row = abs(int(sum(diff_list) / len(diff_list)))
    # print("adj_row :", adj_row)

    count3 = 0
    kk = []
    i = 0
    for n in range(i, len(sorted_list)):
        for m in range(n+1, len(sorted_list)):
            if((sorted_list[m][1][4] <= max_list_x) and ((sorted_list[n][1][1] + (sorted_list[n][1][3]/2))>= sorted_list[m][1][1]) and ((sorted_list[n][1][5] + (sorted_list[n][1][3]/2))>= sorted_list[m][1][5])):
                count3 = count3 + 1
                continue
            else:
                kk.append(m - 1)
                i=n
                break

    kk.append(sorted_list.index(sorted_list[-1]))
    kk = list(dict.fromkeys(kk))
    # print('kk:', kk)

    def swap_x(one, two):
        temp = sorted_list[one]
        sorted_list[one] = sorted_list[two]
        sorted_list[two] = temp

    def sort_x(x, y):
        for n in range(x, y):
            min = n
            for m in range(n + 1, y + 1):
                if ((sorted_list[m][1][0]) < (sorted_list[min][1][0])):
                    min = m
            swap_x(n, min)

    for n in range(0, len(kk)):
        if (n == 0):
            sort_x(0, kk[n])
        if (n != 0):
            sort_x(kk[n - 1] + 1, kk[n])

    def correcting(x, y):
        for n in range(x, y):
            for m in range(n + 1, y + 1):
                sorted_list[m][1][1] = sorted_list[n][1][1]

    for i in range(0, len(kk)):
        if (i == 0):
            correcting(0, kk[i])
        if (i != 0):
            correcting(kk[i - 1] + 1, kk[i])

    print("sorted_list_x:", sorted_list)

    # identify relationship among the elements

    for n in range(0, len(sorted_list)):
        if (sorted_list[n][0][1] == 'RB'):
            for m in range(n + 1, len(sorted_list)):
                if (len(sorted_list[m][0]) >= 2):
                    if (sorted_list[m][0][1] == 'TEXT'):
                        sorted_list.insert(n + 1, sorted_list.pop(m))
                        sorted_list[m][0].append('classified')
                        # sorted_list[n+1][0].append('classified')
                        break
                    else:
                        continue


    for n in range(0, len(sorted_list)):
        if (sorted_list[n][0][1] == 'CB'):
            for m in range(n + 1, len(sorted_list)):
                if (len(sorted_list[m][0]) >= 2):
                    if (sorted_list[m][0][1] == 'TEXT'):
                        sorted_list.insert(n + 1, sorted_list.pop(m))
                        sorted_list[m][0].append('classified')
                        # sorted_list[n+1][0].append('classified')
                        break
                    else:
                        continue

    print("classified:", sorted_list)

    founded_labels = []
    founded_labels_distance = []
    founded_labels_2 = []
    founded_labels_distance_2 = []

    for n in range(0, len(sorted_list) - 1):
        if (sorted_list[n][0][1]) == 'RB':
            start_of_radio_button = sorted_list[n][1][0]
            end_of_label_of_radio_button = sorted_list[n+1][1][4]
            button_height = sorted_list[n][1][3]
            button_plus_label_width = end_of_label_of_radio_button - start_of_radio_button
            left_point = start_of_radio_button - (button_plus_label_width / 4)
            right_point = end_of_label_of_radio_button + (button_plus_label_width / 4)

            for m in range(0, len(sorted_list)):
                if ((sorted_list[m][1][0] > left_point) and (sorted_list[m][1][4] < right_point) and (
                        sorted_list[m][0][1] == 'TEXT') and (sorted_list[m][1][5] < sorted_list[n][1][1])):
                    founded_labels.append(m)
                    founded_labels_distance.append(sorted_list[n][1][1] - sorted_list[m][1][5])
            # print("founded_labels:",founded_labels)
            # print("founded_labels_distance:",founded_labels_distance)

            if (len(founded_labels_distance) > 0):
                nearest_top_label = founded_labels[founded_labels_distance.index(min(founded_labels_distance))]
            # print("nearest_top_label:",nearest_top_label)


            # top_point = sorted_list[n][1][1] - button_height / 2
            # bottom_point = sorted_list[n][1][5] + button_height / 2

            top_point = sorted_list[n][1][5] + button_height / 2
            bottom_point = sorted_list[n][1][1] - button_height / 2

            for m in range(0, len(sorted_list)):
                if ((sorted_list[m][1][1] > top_point) and (sorted_list[m][1][5] < bottom_point) and
                        (sorted_list[m][0][1] == 'TEXT') and  (sorted_list[m][1][0] < sorted_list[n][1][0]) and
                        (len(sorted_list[m][0]) == 2)):
                    founded_labels_2.append(m)
                    founded_labels_distance_2.append(sorted_list[n][1][0] - sorted_list[m][1][4])

            if (len(founded_labels_distance) > 0):

                i = nearest_top_label
                if (len(founded_labels_2) == 0):
                    for m in range(0, len(sorted_list)):
                        if ((sorted_list[m][0][1] == 'RB') and
                                (sorted_list[m][1][0] > left_point and sorted_list[m][1][4] < right_point) and
                                sorted_list[m][1][1] > sorted_list[nearest_top_label][1][5]):
                            sorted_list.insert(i + 1, sorted_list.pop(m))
                            sorted_list.insert(i + 2, sorted_list.pop(m + 1))
                            i = i + 2

                    founded_labels.clear()
                    founded_labels_2.clear()
                    founded_labels_distance.clear()
                    founded_labels_distance_2.clear()
            # print(sorted_list)


    label_count = 0
    input_count = 0

    for n in range(0, len(sorted_list)):
        if (len(sorted_list[n][0]) == 2):
            if ((sorted_list[n][0][1] == 'LBL') or (sorted_list[n][0][1] == 'PW')):
                input_count = input_count + 1
            if ((sorted_list[n][0][1] == 'TEXT') and (len(sorted_list[n][0]) == 2) and (
                    (sorted_list[n - 1][0][1] != 'RB') and (sorted_list[n + 1][0][1] != 'RB') and
                    (sorted_list[n + 1][0][1] != 'DD') and (sorted_list[n - 1][0][1] != 'CB') and
                    (sorted_list[n + 1][0][1] != 'CB'))):
                label_count = label_count + 1

                if (label_count == input_count):
                    top_left_n = sorted_list[n][1][0]
                    top_right_n = sorted_list[n][1][4]
                    top_left_n1 = sorted_list[n - 1][1][0]
                    top_right_n1 = sorted_list[n - 1][1][4]

                    sorted_list[n][1][0] = top_left_n1
                    sorted_list[n][1][4] = top_right_n1

                    sorted_list[n - 1][1][0] = top_left_n
                    sorted_list[n - 1][1][4] = top_right_n
                    sorted_list.insert(n - 1, sorted_list.pop(n))
                    sorted_list[n][0].append('classified')

                if (label_count != input_count):
                    for m in range(n + 1, len(sorted_list)):
                        if (sorted_list[m][0][1] == 'RB'):
                            break
                        if (sorted_list[m][0][1] == 'CB'):
                            break
                        if (sorted_list[m][0][1] == 'DD'):
                            break
                        if ((sorted_list[m][0][1] == 'LBL') or (sorted_list[m][0][1] == 'PW')):
                            sorted_list.insert(n + 1, sorted_list.pop(m))
                            sorted_list[n][0].append('classified')
                            break
                        else:
                            continue

    for n in range(0, len(sorted_list)):
        if (len(sorted_list[n][0]) == 2):
            if (sorted_list[n][0][1] == 'TEXT'):
                for m in range(n + 1, len(sorted_list)):
                    if (sorted_list[m][0][1] == 'RB'):
                        break
                    if (sorted_list[m][0][1] == 'CB'):
                        break
                    if ((sorted_list[m][0][1] == 'LBL') or (sorted_list[m][0][1] == 'PW')):
                        break
                    if (sorted_list[m][0][1] == 'DD'):
                        sorted_list.insert(n + 1, sorted_list.pop(m))
                        sorted_list[n][0].append('classified')
                        break
                    else:
                        continue

    # print("sorted_list:", sorted_list)

    group_id = 1
    for n in range(0, len(sorted_list)):
        if (sorted_list[n][0][1] == 'IMG') or (sorted_list[n][0][1] == 'HPL') or (sorted_list[n][0][1] == 'HPLINK') or (
                sorted_list[n][0][1] == 'BTN'):
            sorted_list[n].append(group_id)
            group_id = group_id + 1

        # checkbox and label or paragraph
        if (sorted_list[n][0][1] == 'CB') and ((sorted_list[n + 1][0][1] == 'TEXT') or (sorted_list[n + 1][0][1] == 'HPLINK')):
            sorted_list[n].append(group_id)
            group_id = group_id + 1

        # label and text, password, paragraph
        if (sorted_list[n][0][1] == 'TEXT') and (
                (sorted_list[n + 1][0][1] == 'LBL') or (sorted_list[n + 1][0][1] == 'HPLINK') or (
                sorted_list[n + 1][0][1] == 'PW')):
            sorted_list[n].append(group_id)
            for m in range(n + 1, len(sorted_list)):
                if ((sorted_list[m][0][1] == 'LBL') or (sorted_list[m][0][1] == 'PW') or (sorted_list[m][0][1] == 'HPLINK')):
                    sorted_list[m].append(group_id)
                    group_id = group_id + 1
                else:
                    break

        # label and dropdown
        if ((sorted_list[n][0][1] == 'TEXT') and (sorted_list[n + 1][0][1] == 'DD')):
            sorted_list[n].append(group_id)
            for m in range(n + 1, len(sorted_list)):
                if (sorted_list[m][0][1] == 'DD'):
                    sorted_list[m].append(group_id)
                else:
                    group_id = group_id + 1
                    break

        # label and radio button
        if ((sorted_list[n][0][1] == 'TEXT') and (len(sorted_list[n][0]) == 2) and (sorted_list[n + 1][0][1] == 'RB')):
            sorted_list[n].append(group_id)
            for m in range(n + 1, len(sorted_list)):

                if ((sorted_list[m][0][1] == 'LBL') or (sorted_list[m][0][1] == 'PW') or (
                        sorted_list[m][0][1] == 'CB') or (sorted_list[m][0][1] == 'DD')):
                    break

                if (sorted_list[m][0][1] == 'RB'):
                    for i in range(m, len(sorted_list), 2):
                        if ((sorted_list[i][0][1] == 'RB') and (sorted_list[i + 1][0][1] == 'TEXT') and (
                                len(sorted_list[i + 1][0]) == 3)):
                            sorted_list[i].append(group_id)
                            continue
                        else:
                            break

                else:
                    group_id = group_id + 1
                    break
    # print("group_id:",sorted_list)

    # remove radio and check box labels
    radio_count = 0
    for n in range(0, len(sorted_list)):
        if (sorted_list[n][0][1] =='RB'):
            radio_count = radio_count + 1

    checkbox_count = 0
    for n in range(0, len(sorted_list)):
        if (sorted_list[n][0][1] == 'CB'):
            checkbox_count = checkbox_count + 1

    if (radio_count > 0):
        for n in range(0, len(sorted_list) - radio_count):
            if (sorted_list[n][0][1] == 'RB'):
                sorted_list[n][0][0] = sorted_list[n + 1][0][0]
                sorted_list.pop(n + 1)

    if (checkbox_count > 0):
        for n in range(0, len(sorted_list) - checkbox_count):
            if (sorted_list[n][0][1] == 'CB'):
                sorted_list[n][0][0] = sorted_list[n + 1][0][0]
                sorted_list.pop(n + 1)

    for n in range(0, len(sorted_list)):
        width = sorted_list[n][1][2]
        left_boundary = sorted_list[n][1][0] - width / 2
        right_boundary = sorted_list[n][1][4] + width / 2

        height = sorted_list[n][1][3]
        upper_boundary = sorted_list[n][1][1] - height / 4
        lower_boundary = sorted_list[n][1][1] + height / 4

        item_count = 0
        for i in range(0, len(sorted_list)):
            item_width = sorted_list[i][1][3]
            # item_height = sorted_list[i][1][3]
            # top_middle = sorted_list[i][1][0] + item_width / 2
            top_middle = sorted_list[i][1][1] + item_width/2

            if (top_middle > upper_boundary and top_middle < lower_boundary):
                item_count = item_count + 1

        if (item_count == 2):
            for m in range(0, len(sorted_list)):
                quarter_1 = sorted_list[n][1][3] / 4
                upper_boundary_1 = sorted_list[n][1][1] - quarter_1
                lower_boundary_1 = sorted_list[n][1][1] + quarter_1

                item_count_1 = 0
                for j in range(0, len(sorted_list)):
                    item_width = sorted_list[j][1][3]
                    # item_height = sorted_list[j][1][3]
                    top_middle = sorted_list[j][1][0] + item_width / 2
                    # mid_width = sorted_list[j][1][0] + item_width/2

                    if (top_middle > upper_boundary_1 and top_middle < lower_boundary_1):
                        item_count = item_count + 1

                if (item_count_1 == 2):
                    if ((sorted_list[m][1][0] > left_boundary) and (sorted_list[m][1][4] < right_boundary)):
                        sorted_list[m][1][0] = sorted_list[n][1][0]
                        sorted_list[m][1][4] = sorted_list[n][1][4]

                if (item_count_1 == 1) and sorted_list[m][0][1] == 'RB':
                    if (sorted_list[m][1][0] > left_boundary) and (sorted_list[m][1][4] < right_boundary):
                        sorted_list[m][1][0] = sorted_list[n][1][0]
                        sorted_list[m][1][4] = sorted_list[n][1][4]

                if (item_count_1 == 1) and sorted_list[m][0][1] == 'CB':
                    if (sorted_list[m][1][0] > left_boundary) and (sorted_list[m][1][4] < right_boundary):
                        sorted_list[m][1][0] = sorted_list[n][1][0]
                        sorted_list[m][1][4] = sorted_list[n][1][4]

    for n in range(0, len(sorted_list)):
        sorted_list[n][1].pop(2)
        sorted_list[n][1].pop(2)

    return sorted_list, max_list_y

    # print("sorted_list_last:", sorted_list)

shapes = input_array()
    # print(len(shapes))
final_output = {}
all_page_names = []

for page_number in range(0, len(shapes)):
    all_page_names.append(shapes[page_number][0][0])
    # print("all_page_names:",all_page_names)

for page_number in range(0, len(shapes)):

    sorted_list, max_list_y = mappingOnePage(shapes[page_number][1])




    page_width = shapes[page_number][0][1]
    # page_width=1000

    increase_ratio = (1366 / page_width) * 100

    for n in range(0, len(sorted_list)):
        sorted_list[n][1][0] = sorted_list[n][1][0] * (increase_ratio / 100)
        sorted_list[n][1][2] = sorted_list[n][1][2] * (increase_ratio / 100)

    for n in range(0, len(sorted_list)):

        if ((sorted_list[n][0][1] == 'HPLINK') and (sorted_list[n - 1][0][1] != 'TEXT')):
            word_list = sorted_list[n][0][0].split()
            word_count = len(word_list)
            letter_count = 0
            width = sorted_list[n][1][2] - sorted_list[n][1][0]
            height = sorted_list[n][1][3] - sorted_list[n][1][1]

            for m in range(0, len(word_list)):
                for i in range(0, len(word_list[m])):
                    letter_count = letter_count + 1

            pixels_of_letter = letter_count * 10.0
            ratio = pixels_of_letter / width

            if (word_count > 10):
                sorted_list[n][0].append(('p1'))

            else:
                if (height >= 135):
                    sorted_list[n][0].append('h1')
                if (height < 130 and height >= 100):
                    sorted_list[n][0].append('h2')
                if (height < 120 and height >= 100):
                    sorted_list[n][0].append('h3')
                if (height < 100 and height >= 85):
                    sorted_list[n][0].append('h4')
                if (height < 85 and height >= 65):
                    sorted_list[n][0].append('h5')
                if (height < 65 and height >= 50):
                    sorted_list[n][0].append('h6')
                if (height < 50):
                    sorted_list[n][0].append('p')

                if (ratio > 0.2):
                    height_of_item = ( sorted_list[n][1][1] + sorted_list[n][1][3]) / 2
                    upper_level = sorted_list[n][1][1] - height_of_item / 2
                    lower_level = sorted_list[n][1][3] + height_of_item / 2
                    countt = 0
                    for i in range(0, len(sorted_list)):
                        if ((sorted_list[i][1][1] > upper_level) and (sorted_list[i][1][3] < lower_level)):
                            countt = countt + 1

                    if (countt == 1):
                        if (sorted_list[n][1][0] < 460):
                            sorted_list[n][0].append('justify')

                        if (sorted_list[n][1][0] > 460 and sorted_list[n][1][0] < 920):
                            sorted_list[n][0].append('center')

                else:
                    sorted_list[n][0].append('center')

        else:
            sorted_list[n][0].append('p')
            sorted_list[n][0].append('left')

    print("before_json:", sorted_list)


    # JSON format

    nb_of_images = 1
    nb_of_paragraphs = 1
    nb_of_labels = 1
    nb_of_texts = 1
    nb_of_passwords = 1
    nb_of_radios = 1
    nb_of_checks = 1
    nb_of_dropdowns = 1
    nb_of_hyperlinks = 1
    nb_of_buttons = 1
    hyper = 1

    data = {}

    for n in range(0, len(sorted_list)):
        top = 0

        if ((sorted_list[n][1][1] / max_list_y) * 100) == 0:
            top = str(int((((sorted_list[n][1][1]) / max_list_y) * 100))) + '%'
        elif (((sorted_list[n][1][1] / max_list_y) * 100) < 10 and ((sorted_list[n][1][1] / max_list_y) * 100) > 1):
            top = '0' + str(int((((sorted_list[n][1][1]) / max_list_y) * 100))) + '%'
        else:
            top = str(int((((sorted_list[n][1][1]) / max_list_y) * 100))) + '%'

        if (sorted_list[n][0][1] == 'IMG'):
            data[sorted_list[n][0][1] + '-' + str(nb_of_images)] = {
                'type': 'img',
                'groupId': str(sorted_list[n][2]),
                'text': ' ',
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_images = nb_of_images + 1

        if (sorted_list[n][0][1] == 'HPLINK'):
            data[sorted_list[n][0][1] + '-' + str(nb_of_paragraphs)] = {
                'type': str(sorted_list[n][0][-2]),
                'groupId': str(sorted_list[n][2]),
                'alignment': str(sorted_list[n][0][-1]),
                'text': sorted_list[n][0][0],
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_paragraphs = nb_of_paragraphs + 1

        if (sorted_list[n][0][1] == 'TEXT'):
            data[sorted_list[n][0][1] + '-' + str(nb_of_labels)] = {
                'type': 'label',
                # 'groupId': str(sorted_list[n][2]),
                'groupId': '',
                'text': sorted_list[n][0][0],
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_labels = nb_of_labels + 1

        if (sorted_list[n][0][1] == 'LBL'):
            data[sorted_list[n][0][1] + '-' + str(nb_of_texts)] = {
                'type': 'text',
                'groupId': str(sorted_list[n][2]),
                'text': '',
                'placeholder': 'Type your',
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_texts = nb_of_texts + 1

        if (sorted_list[n][0][1] == 'PW'):
            data[sorted_list[n][0][1] + '-' + str(nb_of_passwords)] = {
                'type': 'password',
                'groupId': str(sorted_list[n][2]),
                'text': '',
                'placeholder': 'Type your Password',
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_passwords = nb_of_passwords + 1

        if (sorted_list[n][0][1] == 'RB'):

            for nn in range(n - 1, n - 3, -1):
                if (sorted_list[nn][0][1] == 'TEXT'):
                    r_m_label = sorted_list[nn][0][0]
                    # print("r_m_label",r_m_label)
                    break
                else:
                    continue

            data[sorted_list[n][0][1] + '-' + str(nb_of_radios)] = {
                'type': 'radio',
                # 'name': r_m_label,
                'groupId': '',
                'text': sorted_list[n][0][0],
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_radios = nb_of_radios + 1

        if (sorted_list[n][0][1] == 'CB'):
            data[sorted_list[n][0][1] + '-' + str(nb_of_checks)] = {
                'type': 'checkbox',
                'groupId': str(sorted_list[n][5]),
                'text': sorted_list[n][0][0],
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_checks = nb_of_checks + 1

        if (sorted_list[n][0][1] == 'DD'):

            for nn in range(n - 1, n - 3, -1):
                if (sorted_list[nn][0][1] == 'TEXT'):
                    d_m_label = sorted_list[nn][0][0]
                    # print("d_m_label",d_m_label)
                    break
                else:
                    d_m_label = "null"
                    continue

            data[sorted_list[n][0][1] + '-' + str(nb_of_dropdowns)] = {
                'type': 'dropdown',
                'groupId': str(sorted_list[n][2]),
                'text': d_m_label,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'top': top,
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
                'option': {
                    'text': sorted_list[n][0][0],
                    'type': 'option',
                    'values': [sorted_list[n][0][0], 'option2', 'option3,', ]
                }
            }
            nb_of_dropdowns = nb_of_dropdowns + 1

        if (sorted_list[n][0][1] == 'HPL'):
            data[sorted_list[n][0][1] + '-' + str(nb_of_hyperlinks)] = {
                'type': 'a',
                'groupId': str(sorted_list[n][2]),
                'href': str(hyper) + ".html",
                'text': sorted_list[n][0][0],
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_hyperlinks = nb_of_hyperlinks + 1
            hyper = hyper + 1

        if (sorted_list[n][0][1] == 'BTN'):
            data[sorted_list[n][0][1] + '-' + str(nb_of_buttons)] = {
                'type': 'submit',
                'groupId': str(sorted_list[n][2]),
                'text': sorted_list[n][0][0],
                'top': top,
                'left': str(int(((sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'width': str(int(((sorted_list[n][1][2] - sorted_list[n][1][0]) / 1366) * 100)) + '%',
                'height': str(int(((sorted_list[n][1][3] - sorted_list[n][1][1]) / max_list_y) * 100)) + '%',
            }
            nb_of_buttons = nb_of_buttons + 1

    final_output[all_page_names[page_number]] = data

print(final_output)

import json
#
# shapes = input_array()
# # print(len(shapes))
# final_output = {}
# all_page_names = []
#
# for page_number in range(0, len(shapes)):
#     all_page_names.append(shapes[page_number][0])
# # print(all_page_names)
#
# for page_number in range(0, len(shapes)):
#     if(len(shapes[page_number]) > 1):
#          final_output[all_page_names[page_number]] = mappingOnePage(shapes[page_number][1])
with open("../InputFiles/mapping_layouts.json", "w") as outfile:
    json.dump(final_output, outfile, indent=8)

# print("final_output;",final_output[all_page_names[1]])
# print("final_output;", shapes[1][1])
# print("final_output;", shapes[0][1])
# print(mappingOnePage(shapes[0][1]))
with open('../InputFiles/mapping_layouts.json') as json_data:
    loaded_json = json.load(json_data)

page_list = []

for i in range(0, len(loaded_json) + 1):
    for key in loaded_json.keys():
        page_list.append(key)
        for z in loaded_json[page_list[i]]:
            rel_name = z.split('-')
            if (rel_name[0] == 'HPL'):
                for x in loaded_json[page_list[i]][z]:
                    json_text = loaded_json[page_list[i]][z]['text']
                    for pp in range(0, len(all_page_names)):
                        if (all_page_names[pp] == json_text):
                            for x in loaded_json[page_list[i]][z]:
                                loaded_json[page_list[i]][z]['href'] = all_page_names[pp] + '.html'
                                with open("../InputFiles/mapping_layouts.json", "w") as jsonFile:
                                    json.dump(loaded_json, jsonFile, indent=8)
                                break

#
# # from mapping_and_layout.code import max_y
# #
# # print(ML.mapping(all_page_data)) # call mapping and layout main method
# #
# #
# # print("--------------------------------------")
# # print("Success Mapping and Layout Design")
